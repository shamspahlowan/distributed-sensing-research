"""Milestone 0: look at the signals before training anything.

Predict first (write it in NOTES.md):
  - Which two modulations will look most alike in the time domain?
  - What shape does IQ imbalance turn a QPSK constellation into? What does DC offset do?

Outputs results/m0_time_domain.png and results/m0_receivers.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from lab.radio import MODULATIONS, RECEIVERS, SPS, generate

OUT = Path("results")


def time_domain():
    X, y, _ = generate(1, [18], seed=1)
    fig, axes = plt.subplots(2, 4, figsize=(14, 5), sharex=True, sharey=True)
    for ax, label in zip(axes.ravel(), range(len(MODULATIONS))):
        x = X[y == label][0]
        ax.plot(x[0], lw=1, label="I")
        ax.plot(x[1], lw=1, label="Q")
        ax.set_title(MODULATIONS[label])
    axes[0, 0].legend(loc="upper right")
    fig.suptitle("One example per modulation at 18 dB SNR (with fading and frequency offset)")
    fig.tight_layout()
    fig.savefig(OUT / "m0_time_domain.png", dpi=120)


def receivers():
    qpsk = MODULATIONS.index("QPSK")
    fig, axes = plt.subplots(1, len(RECEIVERS), figsize=(4 * len(RECEIVERS), 4), sharex=True, sharey=True)
    for ax, (name, rx) in zip(axes, RECEIVERS.items()):
        X, y, _ = generate(40, [30], receiver=rx, seed=2, channel=False)
        x = X[y == qpsk]
        # Sampling every SPS-th sample lands near symbol centres for some examples and between
        # symbols for others, so the clusters are fuzzy even for the ideal receiver.
        ax.scatter(x[:, 0, ::SPS].ravel(), x[:, 1, ::SPS].ravel(), s=2, alpha=0.4)
        ax.set_title(f"{name}\n{rx.iq_gain_db} dB, {rx.iq_phase_deg} deg, dc {rx.dc_offset}")
        ax.set_aspect("equal")
        ax.axhline(0, color="grey", lw=0.5)
        ax.axvline(0, color="grey", lw=0.5)
    fig.suptitle("QPSK at 30 dB, no channel: only the receiver differs")
    fig.tight_layout()
    fig.savefig(OUT / "m0_receivers.png", dpi=120)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    time_domain()
    receivers()
    print("wrote", OUT / "m0_time_domain.png", "and", OUT / "m0_receivers.png")
