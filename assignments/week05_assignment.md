---
title: "Week 5 Assignment: Risk Modelling and Portfolio Optimization"
week: 5
author: "Praveen Kumar"
date: 2025-10-07
duration: "4-6 hours"
difficulty: "Intermediate"
points: 100
prerequisites: ["Week 4: Time Series Forecasting", "Python Programming", "Statistics"]
tags: ["portfolio-optimization", "risk-modelling", "monte-carlo", "var", "sharpe-ratio"]
version: v1.0
---

# Week 5 Assignment: Risk Modelling and Portfolio Optimization using Python

## Objective
Quantify and optimize financial portfolio risk using Modern Portfolio Theory, Monte Carlo simulation, and advanced risk metrics. Build a comprehensive portfolio optimization tool that demonstrates mastery of risk-return trade-offs in finance.

---

## Dataset Requirements

### Primary Data Source
- **Assets**: Select 5-7 stocks or ETFs from different sectors
- **Suggested Options**: 
  - Technology: AAPL, MSFT, GOOG
  - Finance: JPM, BAC, GS
  - Healthcare: JNJ, PFE, UNH
  - Energy: XOM, CVX
  - Consumer: AMZN, TSLA, WMT
- **Time Period**: 2019-01-01 to 2024-01-01 (5 years)
- **Data Source**: Yahoo Finance via `yfinance` library

### Data Requirements
- Daily adjusted closing prices
- Minimum 1000 trading days
- Handle missing data appropriately
- Calculate daily returns for analysis

---

## Assignment Tasks

### Task 1: Data Collection and Preprocessing (10 points)

**Requirements:**
1. Load historical price data for your selected assets
2. Calculate daily returns and handle missing values
3. Create summary statistics table showing:
   - Mean annual returns
   - Annual volatilities  
   - Sharpe ratios (assume 2% risk-free rate)
   - Maximum drawdowns
4. Generate correlation matrix and heatmap
5. Provide data quality assessment

**Deliverables:**
- Data loading and cleaning code
- Summary statistics table
- Correlation heatmap visualization
- Brief data quality report (2-3 paragraphs)

---

### Task 2: Monte Carlo Portfolio Simulation (25 points)

**Requirements:**
1. Implement Monte Carlo simulation to generate ≥10,000 random portfolios
2. For each portfolio, calculate:
   - Expected return
   - Volatility (risk)
   - Sharpe ratio
3. Create efficient frontier visualization
4. Identify and highlight key portfolios:
   - Maximum Sharpe ratio
   - Minimum volatility
   - Individual assets
5. Analyze the distribution of Sharpe ratios

**Deliverables:**
- Monte Carlo simulation function
- Efficient frontier scatter plot (colored by Sharpe ratio)
- Statistical analysis of portfolio distributions
- Code documentation and comments

---

### Task 3: Portfolio Optimization (25 points)

**Requirements:**
1. Find the optimal portfolio (maximum Sharpe ratio) using:
   - Monte Carlo results
   - Analytical optimization (scipy.optimize)
2. Compare both methods and discuss differences
3. Display optimal portfolio characteristics:
   - Asset weights and allocations
   - Expected return and volatility
   - Sharpe ratio
4. Create portfolio weights visualization (pie chart or bar chart)
5. Calculate portfolio beta (if using market index as benchmark)

**Deliverables:**
- Optimization implementation (both methods)
- Optimal portfolio summary table
- Portfolio weights visualization
- Method comparison analysis

---

### Task 4: Risk Metrics Calculation (20 points)

**Requirements:**
1. Calculate Value at Risk (VaR) and Conditional VaR (CVaR) at 95% confidence level using:
   - Historical simulation method
   - Parametric method (normal distribution)
   - Monte Carlo simulation method
2. Compare results across methods
3. Create return distribution visualization with VaR/CVaR markers
4. Calculate additional risk metrics:
   - Maximum drawdown
   - Volatility of volatility
   - Downside deviation

**Deliverables:**
- VaR/CVaR calculation functions
- Risk metrics comparison table
- Return distribution histogram with risk thresholds
- Risk interpretation and analysis

---

### Task 5: Visualization and Interpretation (20 points)

**Requirements:**
1. Create comprehensive visualization dashboard including:
   - Efficient frontier with highlighted optimal portfolios
   - Portfolio weights breakdown
   - Risk-return scatter plot for individual assets
   - VaR/CVaR distribution analysis
   - Correlation heatmap
2. Professional styling and clear labels
3. Interpret key findings and insights
4. Discuss diversification benefits observed
5. Compare optimal portfolio vs equal-weighted portfolio

**Deliverables:**
- Multi-panel visualization dashboard
- Written interpretation (1-2 pages)
- Key insights and recommendations
- Discussion of limitations and assumptions

---

## Bonus Challenge 💡 (10 extra points)

Implement advanced portfolio optimization features:

1. **Risk-Free Asset Integration**: Add a risk-free asset and compute the Capital Allocation Line
2. **Constrained Optimization**: Implement portfolio optimization with constraints:
   - No short selling (weights ≥ 0)
   - Maximum weight per asset (≤ 40%)
   - Minimum weight per asset (≥ 5%)
3. **CAPM Analysis**: Calculate alpha and beta for each asset and the optimal portfolio
4. **Backtesting**: Implement simple backtesting to evaluate portfolio performance over time

---

## Grading Rubric

| Criteria | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Improvement (<70%) | Points |
|----------|---------------------|---------------|----------------------|--------------------------|--------|
| **Data Collection & Cleaning** | Complete data pipeline with robust error handling | Good data processing with minor issues | Basic data loading with some gaps | Incomplete or poor data handling | 10 |
| **Monte Carlo Simulation** | Efficient implementation with comprehensive analysis | Good simulation with adequate analysis | Basic simulation with limited analysis | Poor or incomplete simulation | 25 |
| **Portfolio Optimization** | Both methods implemented with detailed comparison | Good optimization with some comparison | Basic optimization with limited analysis | Poor or incomplete optimization | 25 |
| **Risk Metrics (VaR, CVaR)** | Multiple methods with thorough comparison | Good risk calculation with some comparison | Basic risk metrics with limited analysis | Poor or incomplete risk analysis | 20 |
| **Visualization & Interpretation** | Professional, comprehensive visualizations with deep insights | Good visualizations with adequate interpretation | Basic visualizations with some interpretation | Poor visualizations or analysis | 20 |
| **Total** | | | | | **100** |

---

## Deliverables Checklist

### Required Files:
- [ ] **Jupyter Notebook**: `Week5_Assignment_PortfolioOptimization.ipynb`
- [ ] **Report**: `Portfolio_Risk_Insights.pdf` (3-5 pages)
- [ ] **Visualizations**: High-quality plots (saved as PNG/PDF)

### Code Requirements:
- [ ] Proper imports and library versions
- [ ] Reproducible results (set random seeds)
- [ ] Clear documentation and comments
- [ ] Error handling for data issues
- [ ] Professional code structure

### Analysis Requirements:
- [ ] All tasks completed with deliverables
- [ ] Clear interpretation of results
- [ ] Discussion of assumptions and limitations
- [ ] Practical insights and recommendations

---

## Workflow Diagram

```mermaid
graph LR
A[Input Asset Prices] --> B[Calculate Returns & Statistics]
B --> C[Monte Carlo Simulation]
C --> D[Generate Random Portfolios]
D --> E[Calculate Risk & Return Metrics]
E --> F[Identify Optimal Portfolio]
F --> G[Calculate VaR & CVaR]
G --> H[Create Visualizations]
H --> I[Interpret Results & Report]
```

---

## Technical Specifications

### Required Libraries:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from scipy.optimize import minimize
from scipy.stats import norm
import warnings
```

### Key Functions to Implement:
1. `load_portfolio_data()` - Data loading and preprocessing
2. `calculate_portfolio_stats()` - Returns, volatility, correlations
3. `monte_carlo_simulation()` - Random portfolio generation
4. `optimize_portfolio()` - Analytical optimization
5. `calculate_var_cvar()` - Risk metrics calculation
6. `create_visualizations()` - Comprehensive plotting

### Performance Requirements:
- Monte Carlo simulation should complete in <2 minutes
- Handle missing data gracefully
- Generate publication-quality visualizations
- Code should be modular and reusable

---

## Submission Guidelines

### Format:
- **Primary Submission**: Jupyter Notebook (.ipynb)
- **Report**: PDF format, 3-5 pages
- **Plots**: High-resolution images (300 DPI minimum)

### File Naming Convention:
- `Week5_Assignment_[YourName]_PortfolioOptimization.ipynb`
- `Week5_Report_[YourName]_PortfolioRiskInsights.pdf`

### Content Structure:
1. **Executive Summary** (1 paragraph)
2. **Data Analysis** (Task 1 results)
3. **Monte Carlo Results** (Task 2 findings)
4. **Optimization Analysis** (Task 3 results)
5. **Risk Assessment** (Task 4 findings)
6. **Conclusions and Recommendations**

---

## Resources and References

### Essential Reading:
1. **Markowitz, H. (1952)** - "Portfolio Selection" - Journal of Finance
2. **Bodie, Kane & Marcus** - "Investments" (Chapters 6-7)
3. **Hull, J.** - "Risk Management and Financial Institutions"

### Online Resources:
- [QuantStart Portfolio Optimization](https://www.quantstart.com/articles/portfolio-optimization/)
- [Python for Finance - Portfolio Theory](https://pypi.org/project/PyPortfolioOpt/)
- [Yahoo Finance API Documentation](https://pypi.org/project/yfinance/)

### Code Examples:
- Course notebooks from Weeks 1-4
- Scipy optimization documentation
- Matplotlib/Seaborn gallery examples

---

## Support and Office Hours

- **Questions**: Post in course discussion forum
- **Office Hours**: Tuesdays 2-4 PM, Thursdays 10-12 PM
- **Email**: For technical issues only
- **Peer Collaboration**: Encouraged for concepts, not code

---

**Due Date**: [Insert specific date - typically 2 weeks from assignment]  
**Late Penalty**: -10% per day late  
**Academic Integrity**: Individual work required, cite all sources

---

*Week 5 Assignment | Financial ML Bootcamp | Praveen Kumar*