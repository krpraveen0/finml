---
title: "Week 5 Quiz: Risk Modelling & Portfolio Optimization"
week: 5
author: "Praveen Kumar"
date: 2025-10-07
duration: "45 minutes"
total_questions: 6
total_points: 30
passing_score: 24
prerequisites: ["Week 5 Lecture Notes", "Risk Modelling Notebook"]
tags: ["risk-modelling", "portfolio-optimization", "var", "cvar", "sharpe-ratio"]
version: v1.0
---

# Week 5 Quiz: Risk Modelling & Portfolio Optimization

**Instructions:** Answer all questions completely. For multiple choice questions, select the best answer. For code questions, provide working Python code. For short answer questions, provide detailed explanations.

**Time Limit:** 45 minutes  
**Total Points:** 30 points  
**Passing Score:** 24 points (80%)

---

## Question 1 (5 points) - Multiple Choice

**What does Value at Risk (VaR) represent in portfolio risk management?**

A) The expected return of the portfolio over a given time period  
B) The maximum loss expected with a given confidence level over a specific time horizon  
C) The correlation between different assets in the portfolio  
D) The optimal allocation of assets to maximize returns  

**Your Answer:** ___________

---

## Question 2 (5 points) - Multiple Choice

**How is Conditional Value at Risk (CVaR) different from VaR?**

A) CVaR is always smaller than VaR  
B) CVaR measures the expected loss beyond the VaR threshold  
C) CVaR only applies to normally distributed returns  
D) CVaR and VaR are the same measure  

**Your Answer:** ___________

---

## Question 3 (5 points) - Multiple Choice

**What does the Efficient Frontier represent in Modern Portfolio Theory?**

A) The set of portfolios with the highest expected returns regardless of risk  
B) The set of portfolios that offer the maximum expected return for each level of risk  
C) The correlation structure between different assets  
D) The historical performance of individual stocks  

**Your Answer:** ___________

---

## Question 4 (5 points) - Multiple Choice

**How should the Sharpe Ratio be interpreted in portfolio optimization?**

A) Higher Sharpe Ratio indicates worse risk-adjusted performance  
B) Sharpe Ratio measures absolute returns without considering risk  
C) Higher Sharpe Ratio indicates better risk-adjusted performance  
D) Sharpe Ratio only applies to individual assets, not portfolios  

**Your Answer:** ___________

---

## Question 5 (5 points) - Code Question

**Write Python code to compute the portfolio variance given weights 'w' and covariance matrix 'cov_matrix'. Assume both are numpy arrays/matrices.**

```python
# Your code here:




```

**Expected Output:** A single value representing the portfolio variance

---

## Question 6 (5 points) - Short Answer

**Why does diversification reduce unsystematic risk in a portfolio? Explain the relationship between correlation and diversification benefits.**

_Write your answer in the space below (4-6 sentences):_

________________________________________________________________

________________________________________________________________

________________________________________________________________

________________________________________________________________

________________________________________________________________

________________________________________________________________

---

## Answer Key (For Instructor Use Only)

### Question 1
**Correct Answer:** B) The maximum loss expected with a given confidence level over a specific time horizon

**Explanation:** VaR represents the maximum loss expected with a given confidence level (e.g., 95%) over a specific time horizon (e.g., 1 day). For example, a 1-day 95% VaR of $100,000 means there's only a 5% chance of losing more than $100,000 in one day.

### Question 2
**Correct Answer:** B) CVaR measures the expected loss beyond the VaR threshold

**Explanation:** CVaR (Conditional VaR or Expected Shortfall) measures the expected loss given that the loss exceeds the VaR threshold. It provides information about tail risk - the severity of losses when they do occur beyond the VaR level. CVaR is always greater than or equal to VaR.

### Question 3
**Correct Answer:** B) The set of portfolios that offer the maximum expected return for each level of risk

**Explanation:** The Efficient Frontier represents the set of optimal portfolios that offer the highest expected return for each level of risk (volatility). Portfolios on the efficient frontier are considered optimal because they provide the best possible risk-return trade-off. Portfolios below the frontier are sub-optimal.

### Question 4
**Correct Answer:** C) Higher Sharpe Ratio indicates better risk-adjusted performance

**Explanation:** The Sharpe Ratio measures risk-adjusted performance by calculating excess return per unit of risk: (Return - Risk-free Rate) / Volatility. A higher Sharpe Ratio indicates better risk-adjusted performance, meaning the investment provides more return for each unit of risk taken. It's the primary metric used in portfolio optimization.

### Question 5
**Correct Answer:** 
```python
portfolio_variance = np.dot(w.T, np.dot(cov_matrix, w))
```

**Alternative Acceptable Answers:**
- `portfolio_variance = w.T @ cov_matrix @ w`
- `portfolio_variance = np.dot(w, np.dot(cov_matrix, w))`
- `portfolio_variance = w @ cov_matrix @ w.T`

**Explanation:** Portfolio variance is calculated using the quadratic form: w^T * Σ * w, where w is the weight vector and Σ is the covariance matrix. In Python, this is implemented as np.dot(w.T, np.dot(cov_matrix, w)) or using the @ operator: w.T @ cov_matrix @ w.

### Question 6
**Sample Correct Answer:** 

Diversification reduces unsystematic risk because it allows the random, asset-specific risks to cancel out across different holdings. When assets are not perfectly correlated (correlation < 1), their individual price movements don't move in perfect lockstep. The diversification benefit is maximized when correlations are low or negative, as the portfolio volatility becomes less than the weighted average of individual asset volatilities. However, systematic risk (market risk) cannot be diversified away as it affects all assets in the market.

**Key Points for Full Credit:**
- Unsystematic risk is asset-specific and can be diversified away
- Correlation less than 1 enables diversification benefits  
- Lower correlations provide greater risk reduction
- Systematic risk affects all assets and cannot be diversified away
- Portfolio volatility < weighted average of individual volatilities when correlation < 1

---

## Learning Objectives Assessed

This quiz evaluates student understanding of:

1. **Risk Metrics**: Understanding VaR and CVaR concepts and applications
2. **Modern Portfolio Theory**: Comprehending efficient frontier and optimization principles  
3. **Technical Implementation**: Ability to calculate portfolio metrics using Python
4. **Performance Measurement**: Interpreting Sharpe ratio for investment decisions
5. **Diversification Theory**: Understanding the mathematical basis for risk reduction

---

## Grading Rubric

### Multiple Choice Questions (Questions 1-4): 5 points each
- **Correct answer:** 5 points
- **Incorrect answer:** 0 points

### Code Question (Question 5): 5 points
- **Correct implementation:** 5 points
- **Minor syntax errors but correct logic:** 4 points  
- **Partial understanding shown:** 2-3 points
- **Incorrect or no answer:** 0 points

### Short Answer Question (Question 6): 5 points
- **Complete and accurate explanation:** 5 points
- **Good explanation with minor gaps:** 4 points
- **Adequate explanation with some inaccuracies:** 3 points
- **Basic understanding shown:** 2 points
- **Poor or incorrect answer:** 0-1 points

---

## Study Resources

### Required Reading:
- Week 5 Lecture Notes: "Risk Modelling & Portfolio Optimization"
- Week 5 Notebook: `05_risk_modelling.ipynb`

### Additional Resources:
- Markowitz (1952) - Portfolio Selection
- Hull - Risk Management textbook chapters 2-3
- Course slides on Modern Portfolio Theory

### Practice Problems:
- Complete all exercises in the Week 5 notebook
- Review Monte Carlo simulation implementations
- Practice VaR/CVaR calculations by hand

---

*Week 5 Quiz | Financial ML Bootcamp | Praveen Kumar*