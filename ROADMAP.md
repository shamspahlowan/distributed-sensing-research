# Learn-by-building roadmap

One small codebase grows milestone by milestone, from a radio simulator up to the
candidate research question in the README. Every milestone maps to papers in `papers/`.

Why simulate instead of downloading RadioML? Because the question is about *receiver
conditions*, and a simulator lets you turn those conditions (SNR, IQ imbalance, phase
noise, DC offset, frequency offset) up and down on purpose. Real data (RML2018, Wisig)
comes later as a check, not as the starting point.

## How to work each milestone

1. **Predict first.** Before running, write your guess in `NOTES.md` (one line is fine).
2. **Run** the experiment script.
3. **Explain the gap** between your guess and the result. That gap is the learning.
4. **Break one thing** on purpose (a parameter, a loss term) and see if the result moves
   the way you expect.

Run everything with `uv run python -m experiments.<name>`. Results land in `results/`.

## Milestones

| # | Build | Papers | Question to answer |
|---|---|---|---|
| 0 | RF signal simulator with per-receiver hardware impairments | 03, 09 | What do the 8 modulations look like, and what does a "bad receiver" do to a constellation? |
| 1 | CNN modulation classifier, accuracy vs SNR | 03 | Where does accuracy collapse, and which classes get confused? |
| 2 | Cross-receiver test: train on receivers A+B, test on C | 09 | How much does a new receiver alone cost you? |
| 3 | FedAvg across receivers (each receiver = one client) | 01, 09 | Does federating fix the receiver gap, or average it away? |
| 4 | FedMD-style federated distillation on a shared proxy set | 02, 01 | What do you lose by sharing predictions instead of weights? |
| 5 | Selective-FD gates: teacher confidence vs ensemble entropy | 04 | Does teacher confidence actually predict whether a teacher is right? |
| 6 | Deep-ensemble uncertainty at each receiver | 11 | Does ensemble disagreement rise when your receiver gets worse? |
| 7 | Receiver conditions that change over time; stale teachers | 05, 06 | Is "how old is this update" a good proxy for "is it still useful"? |
| 8 | **The research question**: receiver-side gate vs confidence vs staleness gates | all | Can a receiver predict, from its own unlabelled data, whether incoming knowledge will help? |

Milestones 0 and 1 are built. Each later milestone reuses `lab/` and adds one
experiment script.
