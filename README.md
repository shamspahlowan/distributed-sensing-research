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

## Second reading batch

The numbering continues the first reading list. Availability checked on 2026-10-28. A missing number means the PDF could not be retrieved, not that a different paper was substituted.

| No. | Paper | Local availability | Source / saved version |
| --- | --- | --- | --- |
| 07 | FedDHKD: A Lightweight Federated Learning Framework Based on Dynamic Hierarchical Knowledge Distillation for 5G IoT | PDF supplied by user; replaces FedBKD | [DOI](https://doi.org/10.1109/Trustcom66490.2025.00342), IEEE TrustCom 2025 |
| 08 | DaFKD: Domain-Aware Federated Knowledge Distillation | PDF downloaded | [CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/papers/Wang_DaFKD_Domain-Aware_Federated_Knowledge_Distillation_CVPR_2023_paper.pdf) |
| 09 | Domain Generalization for Cross-Receiver Radio Frequency Fingerprint Identification | PDF downloaded | [arXiv v1, 2024](https://arxiv.org/abs/2411.03636v1) |
| 10 | Receiver-Agnostic Radio Frequency Fingerprint Identification via Federated Learning | PDF download blocked | [Publisher](https://ieeexplore.ieee.org/document/11373634/), IEEE TMLCN 2026 |
| 11 | An Uncertainty Quantification Framework for Deep Learning-Based Automatic Modulation Classification | PDF downloaded | [arXiv v2, 2025-12-02](https://arxiv.org/abs/2503.04142v2); first posted 2025, journal issue 2026 |
| 12 | Reliability-Gated RF Consistency Learning for Open-Set Spectrum Sensing | PDF download blocked | [Publisher preview](https://www.sciencedirect.com/science/article/pii/S1874490726003617), online 2026 |

See [access notes](papers/ACCESS_NOTES.md) for the outstanding downloads and DOI links.

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
