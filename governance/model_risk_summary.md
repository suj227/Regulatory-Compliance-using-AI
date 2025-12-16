# Model Risk Summary

## Model Purpose
The model is designed to identify potentially suspicious financial transactions
to support transaction monitoring and regulatory compliance activities.

## Model Type
Supervised machine learning classification model using engineered behavioral
and transactional features.

## Key Risks
- Data is based on a public, anonymized proxy dataset and may not fully reflect
  real-world transaction behavior.
- Class imbalance may impact alert volumes if thresholds are not tuned carefully.
- Model performance may degrade over time due to changes in customer behavior.

## Controls and Mitigations
- Stratified train-test split and out-of-sample evaluation.
- Stability checks comparing training and test performance.
- Threshold-based decisioning to control false-positive rates.
- Feature importance analysis to support explainability.
