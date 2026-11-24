# System-aware trust for FD: paper downloads

These are the papers cited in the doc *System-aware trust for federated distillation on edge hardware* (exported to the repo root as a PDF). Downloads were attempted on 2026-11-23.

- **61 of 75 papers downloaded.** Each file's first page was checked against the expected title.
- **14 could not be downloaded.** They are listed below.
- **2 are already in the repo and were not downloaded again:** Selective-FD is `papers/04_…`, and *Knowledge Distillation in FL: A Practical Guide* is `papers/01_…`.
- **Engineering sources were skipped.** These are the blogs, vendor forums, datasheets and a patent in the doc's "Edge deployment realities" section. The two peer-reviewed journal articles in that section were included, as J01 and J02.

## Naming

`<section><nn>_<short_title>_<year>.pdf`. The prefix follows the doc's sections:

| Prefix | Doc section |
| --- | --- |
| COMM | Second contribution: communication-efficient FD |
| A | Trust and reliability of shared knowledge in FD |
| B | System or context trust in FL |
| C | Security of FD |
| D | FD and FL on constrained hardware and low-power links |
| E | Channel-aware and over-the-air FD |
| F | Precision and quantization heterogeneity |
| G | Drones, satellites and underwater |
| H | Drift, sensor faults and non-stationary data |
| I | Surveys and guides |
| J | Sensor-drift journal articles from "Edge deployment realities" |

Years follow the doc. Some 2026 venue papers were first posted on arXiv in 2025.

ArXiv PDFs are the latest version on the download date. Two files are author or repository copies, not publisher versions:

- **D05:** the Zenodo copy of the IEEE Access article.
- **B05:** the Zenodo copy of the SMC 2025 paper.

## Not downloaded

Gaps in the numbering are these papers. No paywall or bot check was bypassed, and nothing was purchased.

| No. | Paper | Why it failed | Where to get it |
| --- | --- | --- | --- |
| COMM01 | FedDT: Communication-Efficient FL via KD and Ternary Compression (Electronics 2025) | MDPI returned HTTP 403 to scripted requests. The paper is open access. | [MDPI](https://www.mdpi.com/2079-9292/14/11/2183), DOI 10.3390/electronics14112183 |
| COMM04 | Hybrid Logit-Exchange Distillation for Communication-Efficient FL (IEEE ISCT 2025) | Closed access. ResearchGate returned 403. No preprint found. | DOI 10.1109/isct66099.2025.11297334 |
| COMM07 | DistilCacheFL (AAAI 2026) | AAAI's site serves a "not a bot" check page. The paper is open access. OpenAlex lists this AAAI record under the title "Re-architecting Personalized Federated Learning for Demanding Edge Environments", so check it is the paper the doc means. | [AAAI OJS](https://ojs.aaai.org/index.php/AAAI/article/view/39655/43616), DOI 10.1609/aaai.v40i29.39655 |
| COMM11 | Ring-Distill (IEEE TDSC 2026) | The PolyU repository dropped the connection at 1.1 of 2.1 MB on every attempt, so only a broken partial file came down. It was deleted. | [PolyU IRA](https://ira.lib.polyu.edu.hk/bitstream/10397/119108/1/Xiao_Decentralized_Federated_Distillation.pdf) |
| A03 | FedCASKD (Future Internet 2026) | MDPI returned 403. Open access. | [MDPI](https://www.mdpi.com/1999-5903/18/6/285), DOI 10.3390/fi18060285 |
| B02 | Trust-Aware and Energy-Efficient FL for Secure Sensor Networks at the Edge (Sensors 2026) | MDPI and Europe PMC both returned 403. Open access. | [MDPI](https://www.mdpi.com/1424-8220/26/8/2307), [PMC13119933](https://pmc.ncbi.nlm.nih.gov/articles/PMC13119933/) |
| B04 | FedTrust: Modelling Adaptive Trust-Risk for IoT-Enabled Federated Decentralized Systems (IEEE VTC 2025) | Closed access. No open copy found. | DOI 10.1109/vtc2025-spring65109.2025.11174376 |
| D01 | Model-Heterogeneous FL for TinyML in IoT (IEEE ACDSA 2026) | Closed access. The UNISA repository returned 403. | [IRIS UNISA](https://www.iris.unisa.it/handle/11386/4943697), DOI 10.1109/acdsa67686.2026.11468134 |
| D08 | Enhancing Communication-Efficient FL for HAR Through KD (IEEE VTC 2025) | The Trento repository returned 403. | [IRIS UniTN](https://iris.unitn.it/retrieve/7bbe7d29-e1d3-44a6-8674-44faa69c23ad/2025001033.pdf), DOI 10.1109/vtc2025-spring65109.2025.11174325 |
| E04 | Enhancing Collaborative ML in Resource-Limited Networks Through KD and Over-the-Air Computation (IEEE TMC 2025) | The Brunel repository server could not be reached (connection timed out). | [BURA](https://bura.brunel.ac.uk/bitstream/2438/31733/1/FullText.pdf), DOI 10.1109/tmc.2025.3582683 |
| G09 | FedRDR (Drones 2024) | MDPI and Preprints.org both returned 403. Open access. | [MDPI](https://www.mdpi.com/2504-446X/8/2/49), DOI 10.3390/drones8020049 |
| H03 | FL-Based Sensor Fault Classification in Label-Scarce Sensor Networks (IEEE Sensors Journal 2025) | Closed access. The doc's link points to an aggregator page, not the paper. | DOI 10.1109/jsen.2025.3591130 |
| H06 | FedLSTM: FL Framework for Sensor Fault Detection in WSNs (Electronics 2024) | MDPI returned 403. The Bedfordshire repository copy returned HTTP 500. Open access. | [MDPI](https://www.mdpi.com/2079-9292/13/24/4907), DOI 10.3390/electronics13244907 |
| J02 | In situ drift correction for a low-cost NO2 sensor network (RSC Environ. Sci.: Atmos. 2023) | RSC returned 403. Open access. | [RSC](https://pubs.rsc.org/en/content/articlelanding/2023/ea/d2ea00145d), DOI 10.1039/d2ea00145d |

Opening the links in a normal browser will likely work for the open-access ones (COMM01, COMM07, A03, B02, G09, H06, J02, and probably COMM11 and E04). The closed-access ones (COMM04, B04, D01, H03) need institutional access or a copy from the authors. Save any you get under the prefix shown so the numbering stays complete.

Papers remain subject to their authors' and publishers' licenses. This folder does not relicense them.
