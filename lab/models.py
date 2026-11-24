"""Small 1-D CNN for raw I/Q input, in the spirit of O'Shea et al. 2016 but with batch norm
and global pooling so it trains in a minute on a laptop."""

import torch
from torch import nn


class IQNet(nn.Module):
    def __init__(self, n_classes, width=64):
        super().__init__()

        def block(c_in, c_out):
            return nn.Sequential(nn.Conv1d(c_in, c_out, 7, padding=3), nn.BatchNorm1d(c_out), nn.ReLU())

        self.features = nn.Sequential(
            block(2, width),
            block(width, width),
            nn.MaxPool1d(2),
            block(width, 2 * width),
            block(2 * width, 2 * width),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
        )
        self.head = nn.Linear(2 * width, n_classes)

    def forward(self, x):
        return self.head(self.features(x))


def device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")
