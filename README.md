# Accelerating Resource Adequacy: Empirical Analysis Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## 📖 Overview
This repository contains the empirical analysis code accompanying the report: **"Accelerating Resource Adequacy: Fast-Track Interconnection Queues in U.S. Power Markets"**.

Unlike theoretical models, this framework is designed to ingest **real-world interconnection data** (sourced from Lawrence Berkeley National Lab and ISO public queues) to quantify the impact of Accelerated Resource Adequacy Queues (ARQ).

It provides the tools to:
1.  **Model Attrition Risks:** Calculate survival probabilities for generation projects using historical withdrawal data.
2.  **Estimate Reliability Costs:** Compute the *Adaptive System Capacity & Deliverability Evaluation* (ASCDE) metric.
3.  **Simulate Financial Impact:** Quantify the "Queue Risk Premium" and its effect on WACC/NPV for developers.
4.  **Compare ISO Performance:** Benchmark queue throughput across PJM, MISO, SPP, CAISO, and ERCOT.

---

## 📂 Data Sources
This framework relies on public datasets. The following files (included in the `/data` directory or available via download) are required for full functionality:

1.  **LBNL "Queued Up" Dataset (2024/2025 Editions):**
    * *Primary Source:* [Lawrence Berkeley National Lab (LBNL)](https://emp.lbl.gov/queues)
    * *Files used:* `LBNL_Ix_Queue_Data_File_thru2024_v2.csv` (Comprehensive project-level data).
2.  **ISO Specific Interactive Queues:**
    * `MISO_2025_GI_Interactive_Queue.csv`
    * `CAISO_Queue.csv`
    * `ERCOT_Queue.csv`
    * `ISO-NE_Queue.csv`
    * `NYISO_Queue.csv`
3.  **Cost Baselines:**
    * NREL Annual Technology Baseline (ATB) for CapEx/OpEx curves.

---

## 🛠 Repository Structure

```text
├── data/                        # Raw and processed CSV inputs
│   ├── LBNL_Ix_Queue_Data.csv   # Master dataset
│   ├── MISO_Queue.csv           # ISO-specific extracts
│   └── Model_Parameters.csv     # Financial assumptions (WACC, VOLL)
│
├── notebooks/                   # Scripts for interactive analysis
│   ├── 01_Survival_Analysis.py
│   ├── 02_ASCDE_Calculation.py
│   └── 03_Financial_Impact.py
│
├── scripts/                     # Production-ready Python modules
│   ├── ARQ_Survival_Real.py     # Survival analysis engine (lifelines)
│   ├── ASCDE_Real_Cost.py       # Reliability cost calculator
│   └── ISO_Metrics.py           # Comparative visualization tools
│
├── output/                      # Generated plots (Attrition curves, ELCC charts)
├── requirements.txt             # Python dependencies
└── README.md

🚀 Key Modules & Methodology
1. Survival & Attrition Modeling (ARQ_Survival_Real.py)

Methodology: Uses Kaplan-Meier estimators and Weibull distribution fitting to model the probability of a project reaching Commercial Operation (COD) based on its time in the queue.

Application: Segmentation by ISO (e.g., PJM vs. ERCOT) and Technology (Solar vs. Battery) to visualize differential risk profiles.

2. Reliability Valuation (ASCDE_Real_Cost.py)

Methodology: Calculates the Adjusted System-Level Cost of Delivered Electricity (ASCDE).

Formula: ASCDE= 
Delivered Energy
System Cost+(EUE×VOLL)

Application: Determines the "reliability premium" saved by fast-tracking specific firm capacity resources (ARQ candidates) versus the status quo.

3. Financial Impact Analysis (Financial_Impact_Empirical.py)

Methodology: Discounted Cash Flow (DCF) modeling integrating queue delay stochasticity.

Key Insight: Quantifies how queue acceleration (e.g., reducing delay from 4 years to 2 years) lowers the Weighted Average Cost of Capital (WACC) by 50–150 basis points.

💻 Usage
Prerequisites

Install the required scientific computing libraries:

Bash
pip install pandas numpy matplotlib scipy lifelines
Running the Analysis

To generate the attrition curves for PJM using real LBNL data:

Bash
python scripts/ARQ_Survival_Real.py --iso PJM --data data/LBNL_Ix_Queue_Data.csv
To calculate the financial impact of a 2-year delay reduction:

Bash
python scripts/Financial_Impact_Empirical.py --capex 100000000 --delay_reduction 2

Citation & Attribution
If you use this code or data in your research, please cite the primary report and the underlying data providers:

Report: Candler, J. (2025). Accelerating Resource Adequacy: Fast-Track Interconnection Queues in U.S. Power Markets.

Data: Rand, J. et al. (2025). Queued Up: Characteristics of Power Plants Seeking Transmission Interconnection. Lawrence Berkeley National Laboratory.

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details. Disclaimer: This repository is for educational and research purposes. Financial modeling results are indicative and should not be used as investment advice.
