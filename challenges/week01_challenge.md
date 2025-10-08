---
title: "Week 1 Challenge — Advanced Linear Model for Stock Trading"
week: 1
author: "Praveen Kumar"
date: 2025-10-07
difficulty: "Intermediate to Advanced"
estimated_time: "4-6 hours"
tags: ["challenge", "trading", "ridge-regression", "backtesting"]
version: v1.0
---

# Week 1 Challenge — Advanced Linear Model for Stock Trading

## Overview

This open-ended challenge extends the basic linear regression model by incorporating additional features, regularization, and a simple trading strategy. You'll build a more sophisticated model and evaluate its potential for generating trading profits.

**Challenge Level:** Intermediate to Advanced  
**Estimated Time:** 4-6 hours  
**Prerequisites:** Completion of Week 1 materials and assignment

## Challenge Description

**Task:** Extend the linear model to include:
1. 5-day lag features (as before)
2. 5-day rolling volatility feature
3. Ridge regularization to prevent overfitting
4. A simple trading rule based on predicted return signs
5. Performance comparison against buy-and-hold strategy

## Detailed Requirements

### Part 1: Enhanced Feature Engineering (25 points)

Create an enhanced feature set that includes:

1. **Lag Features:** Previous 5 days of returns (Lag_1 through Lag_5)
2. **Rolling Volatility:** 5-day rolling standard deviation of returns
3. **Rolling Mean:** 5-day rolling average of returns
4. **Price Momentum:** 10-day price momentum indicator
5. **Volume Feature:** Normalized trading volume (if available)

**Deliverable:** Function `create_advanced_features(data)` that returns a DataFrame with all features.

### Part 2: Ridge Regression Implementation (25 points)

Implement Ridge regression with:

1. **Hyperparameter Tuning:** Use cross-validation to select optimal alpha (regularization strength)
2. **Feature Scaling:** Properly standardize all features
3. **Model Comparison:** Compare Ridge with standard Linear Regression
4. **Coefficient Analysis:** Analyze how regularization affects feature importance

**Deliverable:** Trained Ridge model with documented hyperparameter selection process.

### Part 3: Trading Strategy Implementation (30 points)

Design and implement a simple trading strategy:

1. **Signal Generation:** Use model predictions to generate buy/sell/hold signals
   - Buy when predicted return > threshold (e.g., 0.5%)
   - Sell when predicted return < -threshold
   - Hold otherwise

2. **Position Sizing:** Implement simple position sizing rules
   - Equal weight positions
   - Optional: Risk-based position sizing

3. **Transaction Costs:** Include realistic transaction costs (e.g., 0.1% per trade)

4. **Risk Management:** Implement basic stop-loss or position limits

**Deliverable:** `TradingStrategy` class with backtesting functionality.

### Part 4: Performance Analysis (20 points)

Conduct comprehensive performance analysis:

1. **Returns Analysis:**
   - Total return vs buy-and-hold
   - Annualized return and volatility
   - Sharpe ratio calculation
   - Maximum drawdown analysis

2. **Trade Analysis:**
   - Number of trades executed
   - Win rate (percentage of profitable trades)
   - Average profit/loss per trade
   - Trade duration analysis

3. **Visualization:**
   - Cumulative returns chart
   - Drawdown periods
   - Trading signals overlay on price chart

**Deliverable:** Comprehensive performance report with visualizations.

## Hints and Guidance

### Technical Hints

1. **Cross-Validation for Time Series:**
   ```python
   from sklearn.model_selection import TimeSeriesSplit
   tscv = TimeSeriesSplit(n_splits=5)
   ```

2. **Ridge Alpha Selection:**
   ```python
   alphas = [0.01, 0.1, 1.0, 10.0, 100.0]
   # Use GridSearchCV with TimeSeriesSplit
   ```

3. **Simple Trading Logic:**
   ```python
   def generate_signals(predictions, threshold=0.005):
       signals = np.where(predictions > threshold, 1,  # Buy
                         np.where(predictions < -threshold, -1, 0))  # Sell/Hold
       return signals
   ```

4. **Performance Metrics:**
   ```python
   def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
       excess_returns = returns - risk_free_rate/252  # Daily risk-free rate
       return np.sqrt(252) * excess_returns.mean() / returns.std()
   ```

### Strategic Hints

1. **Feature Engineering:** Financial indicators often work better when combined (e.g., volatility + momentum)

2. **Regularization:** Start with small alpha values and increase gradually

3. **Trading Thresholds:** Test different threshold values (0.25%, 0.5%, 1.0%) for signal generation

4. **Risk Management:** Consider maximum position sizes and portfolio concentration limits

5. **Realistic Expectations:** Even small improvements over buy-and-hold can be significant in finance

## Evaluation Rubric

### Technical Implementation (60 points)
- **Feature Engineering Quality (15 points):** Appropriate features, proper handling of missing values
- **Ridge Regression Implementation (15 points):** Correct hyperparameter tuning, proper cross-validation
- **Trading Strategy Logic (15 points):** Sound signal generation, realistic transaction costs
- **Code Quality (15 points):** Clean, well-documented, reproducible code

### Analysis and Insights (40 points)
- **Performance Analysis (20 points):** Comprehensive metrics, proper benchmarking
- **Model Interpretation (10 points):** Understanding of feature importance, regularization effects
- **Trading Insights (10 points):** Realistic assessment of strategy viability, risk considerations

## Bonus Extensions (Extra Credit)

### Bonus 1: Multi-Asset Strategy (10 points)
- Extend your strategy to multiple stocks (e.g., AAPL, MSFT, GOOGL)
- Implement portfolio-level risk management
- Compare single-stock vs diversified portfolio performance

### Bonus 2: Alternative Regularization (5 points)
- Implement and compare Elastic Net regularization
- Analyze L1 vs L2 penalty effects on feature selection

### Bonus 3: Advanced Backtesting (10 points)
- Implement walk-forward analysis (retrain model periodically)
- Add slippage and market impact modeling
- Include overnight gap risk in returns calculation

## Submission Guidelines

### Required Files

1. **Jupyter Notebook:** `week1_challenge_[LASTNAME].ipynb`
   - Complete implementation with explanations
   - All code cells executed with outputs
   - Clear section headers matching the challenge parts

2. **Python Module:** `trading_strategy.py`
   - Clean implementation of your TradingStrategy class
   - Reusable functions for feature engineering and backtesting

3. **Results Report:** `challenge_results.pdf`
   - 2-3 page summary of findings
   - Key performance metrics and visualizations
   - Honest assessment of strategy viability

4. **Data Files:** Include any additional data files used

### Submission Format
- ZIP file containing all materials
- Clear file naming with your last name
- Include a README file with setup instructions

## Expected Outcomes

### Realistic Performance Expectations
- **Information Ratio:** 0.1 to 0.5 (modest predictive power)
- **Sharpe Ratio:** 0.8 to 1.2 (accounting for transaction costs)
- **Annual Return:** 8-15% (vs ~10% buy-and-hold for broad market)
- **Win Rate:** 52-58% (slight edge over random)

### Learning Outcomes
- Understanding of regularization in financial models
- Experience with realistic trading strategy implementation
- Appreciation for the challenges of systematic trading
- Skills in comprehensive backtesting and performance analysis

## Common Pitfalls to Avoid

1. **Overfitting:** Don't over-optimize hyperparameters on limited data
2. **Look-ahead Bias:** Ensure all features use only past information
3. **Survivorship Bias:** Be aware if using only currently listed stocks
4. **Transaction Cost Neglect:** Always include realistic trading costs
5. **Data Snooping:** Avoid excessive strategy modification based on backtest results

## Getting Help

- **Discussion Forum:** Use the challenge-specific forum thread
- **Office Hours:** Dedicated challenge office hours available
- **Peer Review:** Optional peer review sessions for feedback

## Assessment Criteria

### Excellence Indicators (90-100 points)
- Sophisticated feature engineering with financial intuition
- Proper hyperparameter optimization with time series considerations
- Realistic trading implementation with comprehensive risk management
- Insightful analysis acknowledging both strengths and limitations

### Proficiency Indicators (70-89 points)
- Solid technical implementation with minor issues
- Adequate performance analysis and benchmarking
- Good understanding of model behavior and trading implications
- Clear presentation of results with honest assessment

### Developing Indicators (50-69 points)
- Basic implementation with some technical errors
- Limited analysis or unrealistic performance claims
- Incomplete consideration of transaction costs or risk management
- Unclear or overly optimistic conclusions

---

**Remember:** The goal is not to create the next hedge fund strategy, but to demonstrate understanding of how machine learning models can be applied to financial problems with appropriate skepticism and rigorous evaluation.

**Good luck, and may your Sharpe ratios be ever in your favor!** 📈