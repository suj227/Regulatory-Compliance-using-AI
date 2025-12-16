# Regulatory Compliance AI – Transaction Surveillance Project

## Objective
Design and validate an AI-driven transaction surveillance model to detect anomalous financial behavior aligned with regulatory compliance monitoring, with appropriate governance and model risk controls.

## Dataset
IEEE-CIS Fraud Detection dataset (public, anonymized financial transactions).
The dataset is reframed as a **transaction surveillance use-case**, analogous to monitoring suspicious activity in regulated financial institutions.

## Problem Statement
Financial institutions are required to monitor high-volume transactions to identify potential misconduct, abnormal behavior, or regulatory risk.  
This project builds analytical controls combining:
- Rule-based surveillance
- Machine learning detection
- Model validation and explainability

## Project Scope
- Transaction-level anomaly detection
- Supervised ML classification
- Governance-aware validation
- Explainable AI for regulatory review

## Folder Structure
- `data/` – Raw and processed datasets
- `notebooks/` – Analysis, modeling, validation
- `src/` – Reusable preprocessing and modeling logic
- `governance/` – Model risk and assumptions documentation

## Governance Considerations
- Class imbalance handled explicitly
- Feature leakage reviewed
- Model explainability documented
- Assumptions and limitations stated

## Tools & Technologies
- Python (pandas, numpy, scikit-learn)

## Disclaimer
This project uses a public dataset and is intended solely for educational and demonstration purposes.


