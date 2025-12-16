# Assumptions and Limitations

## Key Assumptions
- Transaction patterns in the dataset are representative of real monitoring scenarios.
- Engineered features capture meaningful behavioral risk signals.
- Labels provided in the dataset are accurate.

## Limitations
- No real temporal production deployment or live feedback loop.
- No customer-level aggregation beyond available proxy fields.
- Interpretability is limited to feature importance rather than full causal explanations.

## Future Enhancements
- Incorporate time-based validation and drift monitoring.
- Add rule-based overlays to complement model predictions.
- Introduce explainability techniques such as SHAP for deeper insight.
