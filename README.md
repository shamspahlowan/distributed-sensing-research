# Distributed Sensing Research

Personal reading collection exploring federated learning, knowledge distillation, and reliable RF sensing under changing conditions.

## Reading order

1. [Knowledge Distillation in Federated Learning: A Practical Guide (2024)](https://www.ijcai.org/proceedings/2024/0905) — a map of federated distillation approaches.
2. [FedMD: Heterogenous Federated Learning via Model Distillation (2019)](https://arxiv.org/abs/1910.03581) — collaboration between clients with different model architectures.
3. [Convolutional Radio Modulation Recognition Networks (2016)](https://arxiv.org/abs/1602.04105) — an introductory baseline for learning from radio signals.
4. [Selective Knowledge Sharing for Privacy-Preserving Federated Distillation without a Good Teacher (2024)](https://www.nature.com/articles/s41467-023-44383-9) — filtering misleading knowledge.
5. [Federated Learning under Distributed Concept Drift (2023)](https://proceedings.mlr.press/v206/jothimurugesan23a.html) — learning when clients experience changes at different times.
6. [Reviving Stale Updates: Data-Free Knowledge Distillation for Asynchronous Federated Learning (initially posted 2025)](https://arxiv.org/abs/2511.00655) — recovering useful information from stale updates. The downloaded PDF may include later revisions.

PDFs are in `papers/`, numbered in this order. Papers remain subject to their respective authors' and publishers' licenses; this repository does not relicense them.

## Candidate research question

Can a receiver estimate whether shared knowledge will help under its current RF conditions, rather than relying only on teacher confidence or update age?

This is a candidate direction, not an established novelty claim. Further literature review and baseline experiments are needed.

## Reading notes checklist

- What failure does the paper address?
- What is exchanged between clients and server?
- Which assumptions require labels, shared reference data, or stable environments?
- What experimental evidence supports the claims?
- Which relevant conditions were not tested?
- What single experiment could test one assumption?
