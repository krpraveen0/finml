---
title: "Credit Default Prediction with Explainable AI (XAI)"
week: 3
author: "Praveen Kumar"
date: 2025-10-07
objective: "Build a credit scoring model using RandomForest or XGBoost and interpret results with SHAP."
tags: ["challenge", "credit-scoring", "XAI", "SHAP", "finance"]
version: v1.0
---

# Week 3 Challenge — Credit Default Prediction with Explainable AI (XAI)

## Prompt
Build a credit scoring model using RandomForest or XGBoost. Use SHAP to interpret feature impacts. Generate a dashboard-style visualization of SHAP values for the top 10 features. Discuss model fairness and interpretability for financial decisions.

## Deliverables
- Notebook: `Week3_Challenge_XAI_CreditScoring.ipynb`
- Visualization plots (SHAP summary, dependence plots)
- Short summary (insights on interpretability and risk bias)

## Diagram
```mermaid
graph LR
A[Dataset] --> B[Model Training]
B --> C[Prediction + SHAP Analysis]
C --> D[Explainability Dashboard]
D --> E[Business Risk Insights]
```

## Requirements
- Use provided synthetic or Kaggle credit scoring dataset
- Train RandomForest or XGBoost model
- Compute SHAP values for all features
- Visualize top 10 features (summary, dependence plots)
- Discuss fairness (e.g., bias in predictions, impact on protected groups)
- Summarize interpretability findings for business/risk teams

## Success Tips
- Use SEED=42 for reproducibility
- Document all steps and findings
- Use clear, professional visualizations
- Address fairness and regulatory concerns

---
*Challenge designed by Praveen Kumar | Financial ML Bootcamp | Week 3*