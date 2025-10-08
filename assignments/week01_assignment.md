---
title: "Week 1 Assignment — Predicting Next-Day Stock Returns using Linear Regression"
week: 1
author: "Praveen Kumar"
date: 2025-10-07
due_date: "2025-10-14"
points: 100
tags: ["assignment", "linear-regression", "time-series"]
version: v1.0
---

# Week 1 Assignment — Predicting Next-Day Stock Returns using Linear Regression

## Objective

This assignment tests your understanding of financial time series analysis and linear regression modeling. You will build a predictive model for stock returns using historical price data and lag features.

**Learning Goals:**
- Apply feature engineering techniques to financial time series data
- Implement and evaluate linear regression models for return prediction
- Practice proper time series data splitting and validation
- Interpret model results in a financial context

## Dataset Instructions

You have two options for data:

### Option 1: Use yfinance (Recommended)
Download any stock of your choice using the `yfinance` library:
```python
import yfinance as yf
data = yf.download('TICKER_SYMBOL', start='2022-01-01', end='2024-01-01')
```

### Option 2: Use Provided Synthetic Data
If internet access is unavailable, use the provided `data/synthetic/stock_prices.csv` file.

**Suggested Tickers:** AAPL, MSFT, GOOGL, TSLA, SPY, BTC-USD

## Required Skills

- Python programming (pandas, numpy, matplotlib)
- Machine learning with scikit-learn
- Basic understanding of financial returns and time series
- Data visualization and interpretation

## Tasks

Complete the following tasks in order. Submit your work as a Jupyter notebook.

### Task 1: Data Loading and Exploration (15 points)
1. Load stock price data for your chosen ticker
2. Calculate basic statistics (mean, std, min, max) for the closing price
3. Create a time series plot of the stock price over the entire period
4. Calculate and plot daily returns over time

### Task 2: Feature Engineering (25 points)
1. Calculate daily returns: `return_t = (price_t - price_{t-1}) / price_{t-1}`
2. Create lag features for the previous 5 days (Lag_1 through Lag_5)
3. Handle missing values appropriately
4. Display the first 10 rows of your feature matrix
5. Calculate correlation matrix between lag features and target return

### Task 3: Data Splitting (15 points)
1. Split your data chronologically (NOT randomly) into 80% train / 20% test
2. Ensure your split respects the time order of observations
3. Print the date ranges for training and test sets
4. Verify that no future information leaks into the training set

### Task 4: Model Training (20 points)
1. Train a Linear Regression model using the 5 lag features
2. Use proper preprocessing (StandardScaler recommended)
3. Fit the model on the training set only
4. Display the model equation with coefficients

### Task 5: Model Evaluation (15 points)
1. Make predictions on both training and test sets
2. Calculate MSE and R² for both sets
3. Create an "Actual vs Predicted" scatter plot for the test set
4. Analyze whether the model shows signs of overfitting

### Task 6: Results Interpretation (10 points)
1. Identify which lag feature has the strongest predictive power
2. Determine if the model captures momentum or mean-reversion behavior
3. Comment on the practical significance of your R² value
4. Discuss limitations of your approach

## Deliverables

Submit the following files:

1. **Jupyter Notebook** (`week1_assignment_[LASTNAME].ipynb`)
   - Complete implementation of all tasks
   - Clear markdown explanations for each section
   - Well-commented code
   - All output cells should be executed

2. **Visualization** (`prediction_plot.png`) 
   - High-quality "Actual vs Predicted" scatter plot from Task 5
   - Include R² value in the plot title
   - Professional formatting with proper labels

3. **Summary Report** (`week1_summary_[LASTNAME].pdf`)
   - One-page summary of your findings
   - Key statistics (R², MSE, best performing lag)
   - Business interpretation of results
   - Recommendations for model improvement

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Data Loading & Exploration** | 15 | Correct data loading, basic statistics, clear visualizations |
| **Feature Engineering** | 25 | Proper return calculation, lag feature creation, missing value handling |
| **Data Splitting** | 15 | Chronological split, correct train/test proportions, no data leakage |
| **Model Training** | 20 | Correct model implementation, preprocessing, coefficient interpretation |
| **Model Evaluation** | 15 | Appropriate metrics, visualizations, overfitting analysis |
| **Results Interpretation** | 10 | Meaningful insights, practical implications, limitations discussion |

**Bonus Points:**
- Code quality and documentation: +5 points
- Creative visualizations: +3 points
- Additional analysis beyond requirements: +2 points

## Bonus Challenge (Optional - 10 Extra Points)

### Challenge 1: Ridge Regression Comparison
Implement Ridge regression with different regularization strengths (α = 0.1, 1.0, 10.0) and compare performance with your baseline linear regression.

### Challenge 2: Alternative Assets
Try your approach on cryptocurrency data (BTC-USD) and compare the predictability with traditional stocks.

## Submission Guidelines

- **Deadline:** One week from assignment date
- **Format:** Submit via course platform as ZIP file containing all deliverables
- **File Naming:** Use your last name in filenames for easy identification
- **Code Quality:** Ensure all cells run from top to bottom without errors

## Common Pitfalls to Avoid

1. **Random Shuffling:** Never randomly shuffle time series data - this causes data leakage
2. **Look-ahead Bias:** Don't use future information to predict past returns
3. **Overfitting Interpretation:** Low R² values are normal for financial data - don't panic!
4. **Scale Issues:** Remember to standardize features for linear regression
5. **Missing Values:** Handle NaN values from lag feature creation properly

## Getting Help

- Review Week 1 lecture notes and student notebook
- Check the course discussion forum for clarifications
- Office hours: [Insert schedule]
- Email for technical issues: [Insert email]

**Academic Integrity:** This is an individual assignment. You may discuss concepts but must submit your own work.

---

*Good luck! Remember that financial prediction is inherently challenging - focus on demonstrating proper methodology rather than achieving perfect predictions.*