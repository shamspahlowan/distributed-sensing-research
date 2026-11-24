"""Milestone 1: modulation classification vs SNR (O'Shea et al. 2016).

Predict first (write it in NOTES.md):
  - Below what SNR does accuracy fall under 50%?
  - Which pairs will the confusion matrix mix up at high SNR? (O'Shea saw 8PSK/QPSK.)

Outputs results/m1_accuracy_vs_snr.png, results/m1_confusion.png, results/m1.json.
"""

import json
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch

from lab.models import IQNet, device
from lab.radio import MODULATIONS, RECEIVERS, generate
from lab.train import accuracy_by_snr, confusion, fit, predict_proba

OUT = Path("results")
SNRS = list(range(-10, 21, 2))


def main():
    OUT.mkdir(exist_ok=True)
    torch.manual_seed(0)
    rx = RECEIVERS["ideal"]
    t0 = time.time()
    X_tr, y_tr, _ = generate(400, SNRS, receiver=rx, seed=0)
    X_te, y_te, s_te = generate(150, SNRS, receiver=rx, seed=1)
    print(f"data: {len(X_tr)} train / {len(X_te)} test, generated in {time.time() - t0:.1f}s")

    dev = device()
    model = fit(IQNet(len(MODULATIONS)), X_tr, y_tr, dev, epochs=12)
    proba = predict_proba(model, X_te, dev)

    acc = accuracy_by_snr(proba, y_te, s_te)
    overall = float((proba.argmax(1) == y_te).mean())
    print(f"overall test accuracy {overall:.3f}")
    print("  ".join(f"{s:+d}dB:{a:.2f}" for s, a in acc.items()))

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(list(acc), list(acc.values()), marker="o")
    ax.axhline(1 / len(MODULATIONS), color="grey", ls="--", label="chance")
    ax.set(xlabel="SNR (dB)", ylabel="accuracy", ylim=(0, 1), title="IQNet, ideal receiver")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "m1_accuracy_vs_snr.png", dpi=120)

    high = s_te >= 10
    cm = confusion(proba[high], y_te[high], len(MODULATIONS))
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow(cm / cm.sum(1, keepdims=True), cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(len(MODULATIONS)), MODULATIONS, rotation=45)
    ax.set_yticks(range(len(MODULATIONS)), MODULATIONS)
    ax.set(xlabel="predicted", ylabel="true", title="Confusion at SNR >= 10 dB")
    for i in range(len(MODULATIONS)):
        for j in range(len(MODULATIONS)):
            if cm[i, j]:
                ax.text(j, i, cm[i, j], ha="center", va="center", fontsize=7)
    fig.tight_layout()
    fig.savefig(OUT / "m1_confusion.png", dpi=120)

    torch.save(model.state_dict(), OUT / "m1_iqnet.pt")
    (OUT / "m1.json").write_text(json.dumps({"overall": overall, "by_snr": acc, "confusion_high_snr": cm.tolist()}, indent=2))
    print("wrote results/m1_*")


if __name__ == "__main__":
    main()
