"""Synthetic radio signals with per-receiver hardware impairments.

Signal chain for every example (compare O'Shea et al. 2016, eq. 2, and Zhang et al. 2024, eq. 1):

    symbols -> pulse shaping -> multipath channel -> frequency/phase offset -> AWGN
            -> receiver front end (IQ imbalance, DC offset, phase noise) -> unit-power window

Everything up to AWGN is "the world". The last stage is "your receiver", which is what the
research question cares about: two receivers seeing the same transmission produce different
data.
"""

from dataclasses import dataclass

import numpy as np

MODULATIONS = ["BPSK", "QPSK", "8PSK", "16QAM", "64QAM", "PAM4", "CPFSK", "GFSK"]
SPS = 8  # samples per symbol
WINDOW = 128  # samples per example, as in RadioML 2016


@dataclass(frozen=True)
class Receiver:
    """Hardware imperfections of one receiver. All zeros means an ideal receiver."""

    name: str = "ideal"
    iq_gain_db: float = 0.0  # gain mismatch between I and Q branches
    iq_phase_deg: float = 0.0  # I and Q mixers not exactly 90 degrees apart
    dc_offset: float = 0.0  # LO leakage shows up as a constant added to the signal
    phase_noise_std: float = 0.0  # per-sample std (radians) of the oscillator's random walk
    cfo_bias: float = 0.0  # this receiver's own oscillator error, cycles per sample


RECEIVERS = {
    "ideal": Receiver(),
    "rx_a": Receiver("rx_a", iq_gain_db=0.5, iq_phase_deg=2.0, dc_offset=0.02, phase_noise_std=0.005),
    "rx_b": Receiver("rx_b", iq_gain_db=-1.0, iq_phase_deg=-4.0, dc_offset=0.05, phase_noise_std=0.01, cfo_bias=0.002),
    "rx_c": Receiver("rx_c", iq_gain_db=2.0, iq_phase_deg=8.0, dc_offset=0.10, phase_noise_std=0.02, cfo_bias=-0.004),
}


def _constellation(name):
    if name == "BPSK":
        points = np.array([-1, 1], dtype=complex)
    elif name == "QPSK":
        points = np.exp(1j * (np.pi / 4 + np.pi / 2 * np.arange(4)))
    elif name == "8PSK":
        points = np.exp(1j * np.pi / 4 * np.arange(8))
    elif name in ("16QAM", "64QAM"):
        m = int(np.sqrt(int(name[:-3])))
        levels = np.arange(-(m - 1), m, 2)
        points = (levels[:, None] + 1j * levels[None, :]).ravel()
    elif name == "PAM4":
        points = np.array([-3, -1, 1, 3], dtype=complex)
    else:
        raise ValueError(name)
    return points / np.sqrt(np.mean(np.abs(points) ** 2))


def _rrc_taps(beta=0.35, span=6, sps=SPS):
    """Root-raised-cosine pulse: the standard band-limiting filter for digital modulations."""
    t = np.arange(-span * sps, span * sps + 1) / sps
    taps = np.empty_like(t)
    for i, ti in enumerate(t):
        if np.isclose(ti, 0):
            taps[i] = 1 - beta + 4 * beta / np.pi
        elif np.isclose(abs(ti), 1 / (4 * beta)):
            taps[i] = beta / np.sqrt(2) * ((1 + 2 / np.pi) * np.sin(np.pi / (4 * beta)) + (1 - 2 / np.pi) * np.cos(np.pi / (4 * beta)))
        else:
            num = np.sin(np.pi * ti * (1 - beta)) + 4 * beta * ti * np.cos(np.pi * ti * (1 + beta))
            taps[i] = num / (np.pi * ti * (1 - (4 * beta * ti) ** 2))
    return taps / np.sqrt(np.sum(taps**2))


def _convolve_rows(x, h):
    """Full linear convolution of each row of x with h (1-D, or one filter per row)."""
    n = x.shape[1] + h.shape[-1] - 1
    return np.fft.ifft(np.fft.fft(x, n) * np.fft.fft(h, n), n)


def _baseband(name, n, length, rng):
    """n clean complex baseband signals of the given length."""
    n_sym = length // SPS + 16  # extra symbols so the filter edges can be cut away
    if name in ("CPFSK", "GFSK"):
        bits = rng.choice([-1.0, 1.0], size=(n, n_sym))
        freq = np.repeat(bits, SPS, axis=1)
        if name == "GFSK":  # Gaussian-smoothed frequency steps (BT = 0.5), as in Bluetooth
            t = np.arange(-2 * SPS, 2 * SPS + 1) / SPS
            g = np.exp(-2 * (np.pi * 0.5 * t) ** 2 / np.log(2))
            freq = np.real(_convolve_rows(freq, g / g.sum()))[:, 2 * SPS : 2 * SPS + freq.shape[1]]
        phase = np.cumsum(np.pi * 0.5 * freq / SPS, axis=1)  # modulation index h = 0.5
        signal = np.exp(1j * phase)
    else:
        points = _constellation(name)
        symbols = points[rng.integers(len(points), size=(n, n_sym))]
        upsampled = np.zeros((n, n_sym * SPS), dtype=complex)
        upsampled[:, ::SPS] = symbols
        signal = _convolve_rows(upsampled, _rrc_taps())
    start = rng.integers(6 * SPS, signal.shape[1] - length - 6 * SPS, size=n)  # random timing offset
    return signal[np.arange(n)[:, None], start[:, None] + np.arange(length)]


def _channel(x, rng, max_cfo=0.002, n_taps=3):
    """Random multipath fading, carrier frequency offset and phase rotation."""
    n, length = x.shape
    decay = np.exp(-np.arange(n_taps))
    taps = (rng.normal(size=(n, n_taps)) + 1j * rng.normal(size=(n, n_taps))) * np.sqrt(decay / 2)
    taps[:, 0] += 1.0  # a line-of-sight path keeps most examples usable (Rician-like)
    taps /= np.linalg.norm(taps, axis=1, keepdims=True)
    x = _convolve_rows(x, taps)[:, :length]
    cfo = rng.uniform(-max_cfo, max_cfo, size=(n, 1))
    phase0 = rng.uniform(0, 2 * np.pi, size=(n, 1))
    return x * np.exp(1j * (2 * np.pi * cfo * np.arange(length) + phase0))


def _awgn(x, snr_db, rng):
    noise_power = np.mean(np.abs(x) ** 2, axis=1, keepdims=True) / 10 ** (snr_db / 10)
    noise = rng.normal(size=x.shape) + 1j * rng.normal(size=x.shape)
    return x + noise * np.sqrt(noise_power / 2)


def apply_receiver(x, rx, rng):
    """Front-end imperfections of one receiver, applied to already-noisy signals."""
    length = x.shape[1]
    if rx.cfo_bias:
        x = x * np.exp(2j * np.pi * rx.cfo_bias * np.arange(length))
    if rx.phase_noise_std:
        walk = np.cumsum(rng.normal(scale=rx.phase_noise_std, size=x.shape), axis=1)
        x = x * np.exp(1j * walk)
    g = 10 ** (rx.iq_gain_db / 20)
    phi = np.deg2rad(rx.iq_phase_deg)
    mu = (1 + g * np.exp(-1j * phi)) / 2
    nu = (1 - g * np.exp(1j * phi)) / 2
    x = mu * x + nu * np.conj(x)  # IQ imbalance leaks a mirror image of the signal into itself
    return x + rx.dc_offset * (1 + 1j)


def generate(n_per_class_snr, snrs_db, receiver=RECEIVERS["ideal"], seed=0, length=WINDOW, channel=True):
    """Return (X, y, snr): X is float32 (N, 2, length) with I and Q rows, y is class index.

    channel=False skips fading and frequency offset, which is handy for looking at what the
    receiver alone does to a signal.
    """
    rng = np.random.default_rng(seed)
    xs, ys, ss = [], [], []
    for label, name in enumerate(MODULATIONS):
        for snr in snrs_db:
            x = _baseband(name, n_per_class_snr, length, rng)
            if channel:
                x = _channel(x, rng)
            x = _awgn(x, snr, rng)
            x = apply_receiver(x, receiver, rng)
            x /= np.sqrt(np.mean(np.abs(x) ** 2, axis=1, keepdims=True))
            xs.append(np.stack([x.real, x.imag], axis=1))
            ys.append(np.full(n_per_class_snr, label))
            ss.append(np.full(n_per_class_snr, snr))
    return (
        np.concatenate(xs).astype(np.float32),
        np.concatenate(ys).astype(np.int64),
        np.concatenate(ss).astype(np.int64),
    )
