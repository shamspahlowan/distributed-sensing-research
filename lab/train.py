"""Plain supervised training and evaluation, reused by every later milestone."""

import numpy as np
import torch
from torch import nn


def batches(X, y, batch_size, shuffle, rng=None):
    idx = rng.permutation(len(X)) if shuffle else np.arange(len(X))
    for start in range(0, len(X), batch_size):
        b = idx[start : start + batch_size]
        yield torch.from_numpy(X[b]), torch.from_numpy(y[b])


def fit(model, X, y, dev, epochs=10, lr=1e-3, batch_size=256, seed=0, log=print):
    rng = np.random.default_rng(seed)
    model.to(dev)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=lr * 3, total_steps=epochs * -(-len(X) // batch_size))
    loss_fn = nn.CrossEntropyLoss()
    for epoch in range(epochs):
        model.train()
        total, n = 0.0, 0
        for xb, yb in batches(X, y, batch_size, shuffle=True, rng=rng):
            xb, yb = xb.to(dev), yb.to(dev)
            loss = loss_fn(model(xb), yb)
            opt.zero_grad()
            loss.backward()
            opt.step()
            sched.step()
            total += loss.item() * len(xb)
            n += len(xb)
        log(f"epoch {epoch + 1:2d}  train loss {total / n:.3f}")
    return model


@torch.no_grad()
def predict_proba(model, X, dev, batch_size=1024):
    model.eval()
    out = [torch.softmax(model(xb.to(dev)), dim=1).cpu() for xb, _ in batches(X, np.zeros(len(X), np.int64), batch_size, shuffle=False)]
    return torch.cat(out).numpy()


def accuracy_by_snr(proba, y, snr):
    pred = proba.argmax(1)
    return {int(s): float((pred[snr == s] == y[snr == s]).mean()) for s in np.unique(snr)}


def confusion(proba, y, n_classes):
    m = np.zeros((n_classes, n_classes), dtype=int)
    np.add.at(m, (y, proba.argmax(1)), 1)
    return m
