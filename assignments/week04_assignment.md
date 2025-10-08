---
title: "Forecasting Stock Prices using ARIMA, Prophet, and LSTM"
week: 4
author: "Praveen Kumar"
date: 2025-10-07
objective: "Develop, train, and compare three time-series forecasting models for a financial asset."
dataset: "Any stock symbol via yfinance (AAPL, TSLA, TCS, or NIFTY 50). Time range: 2018–2024 (daily data)."
tags: ["assignment", "time-series", "forecasting", "ARIMA", "Prophet", "LSTM"]
version: v1.0
---

# Week 4 Assignment — Forecasting Stock Prices using ARIMA, Prophet, and LSTM

## Objective
Develop, train, and compare three time-series forecasting models (ARIMA, Prophet, LSTM) for a financial asset of your choice.

## Dataset
- **Source**: Use any stock symbol via yfinance (recommended: AAPL, TSLA, TCS, or NIFTY 50)
- **Time Range**: 2018–2024 (daily data)
- **Target**: Close prices or daily returns

## Tasks

### 1. Data Preparation (15 marks)
- Load and clean price data using yfinance
- Handle missing values and outliers
- Compute daily returns if forecasting returns
- Check for stationarity using ADF test
- Create train/test splits (80/20)

### 2. ARIMA Implementation (20 marks)
- Determine optimal (p,d,q) parameters using AIC/BIC
- Fit ARIMA model on training data
- Generate 30-day forecasts
- Visualize predictions vs actual values

### 3. Prophet Implementation (20 marks)
- Format data with 'ds' and 'y' columns
- Fit Prophet model with appropriate seasonality
- Generate 30-day forecasts with confidence intervals
- Plot trend and seasonal components

### 4. LSTM Implementation (25 marks)
- Create supervised learning dataset with lookback window
- Build and train LSTM neural network
- Scale data using MinMaxScaler
- Generate 30-day forecasts
- Inverse transform predictions

### 5. Evaluation & Interpretation (20 marks)
- Calculate RMSE, MAE, MAPE for all models
- Create comparison visualizations
- Discuss which model best fits financial data
- Write one-page report with insights and recommendations

## Deliverables
- **Notebook**: `Week4_Assignment_TimeSeries.ipynb`
- **Plots**: Actual vs Predicted for all three models
- **Report**: One-page summary (PDF/Markdown) with RMSE comparison and insights

## Grading Rubric
| Criteria | Marks | Description |
|----------|-------|-------------|
| Data Preparation | 15 | Data loading, cleaning, stationarity checks |
| ARIMA Implementation | 20 | Model fitting, parameter selection, forecasting |
| Prophet Implementation | 20 | Proper formatting, seasonality, forecasting |
| LSTM Implementation | 25 | Network architecture, training, prediction |
| Evaluation & Interpretation | 20 | Metrics calculation, visualization, insights |
| **Total** | **100** | |

## Bonus Challenge 💡 (+10 points)
Add macroeconomic exogenous variables (USD/INR, Crude Oil, VIX) to:
- ARIMAX model (with external regressors)
- LSTM model (with additional input features)

Compare performance with and without exogenous variables.

## Success Tips
1. **Start Early**: Time series models require iterative tuning
2. **Data Quality**: Ensure clean, consistent data with proper date indexing
3. **Stationarity**: Transform non-stationary series before ARIMA modeling
4. **LSTM Tuning**: Experiment with different lookback windows and architectures
5. **Visualization**: Clear plots are crucial for interpretation

## Technical Requirements
- Use `SEED=42` for reproducibility
- Include error handling for data loading failures
- Document all hyperparameter choices
- Provide clear markdown explanations for each step

---

## Workflow Diagram
```mermaid
graph LR
A[Stock Data] --> B[Model Training]
B --> C[Forecast Generation]
C --> D[Error Metrics]
D --> E[Model Comparison & Insights]
```

## Evaluation Criteria
- **Technical Implementation**: Correct model implementation and parameter tuning
- **Forecast Accuracy**: Low error metrics and realistic predictions
- **Interpretation**: Clear analysis of model strengths/weaknesses
- **Presentation**: Professional visualizations and documentation

---

*Assignment designed by Praveen Kumar | Financial ML Bootcamp | Week 4*