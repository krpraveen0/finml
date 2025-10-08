---
title: "Week 4 Quiz — Time Series Forecasting in Finance"
week: 4
author: "Praveen Kumar"
date: 2025-10-07
duration: "40 minutes"
total_points: 100
version: v1.0
---

# Week 4 Quiz — Time Series Forecasting in Finance

**Instructions:** Complete all questions within the time limit. Show your work for calculations and provide clear explanations for short answer questions.

**Time Limit:** 40 minutes  
**Total Points:** 100

---

## Question 1 (15 points)
**Multiple Choice**

What does the Augmented Dickey-Fuller (ADF) test check for in time series analysis?

A) Autocorrelation in residuals  
B) Stationarity of the time series  
C) Seasonal patterns in the data  
D) Normality of the error terms  

---

## Question 2 (15 points)
**Multiple Choice**

In ARIMA(p,d,q), which component captures the autocorrelation structure?

A) The Integrated (I) component with parameter d  
B) The Moving Average (MA) component with parameter q  
C) The Autoregressive (AR) component with parameter p  
D) All three components equally  

---

## Question 3 (15 points)
**Multiple Choice**

What is the main advantage of Facebook Prophet over ARIMA for financial forecasting?

A) Prophet is faster to train than ARIMA  
B) Prophet automatically handles seasonality and missing data  
C) Prophet always produces more accurate forecasts  
D) Prophet requires less historical data  

---

## Question 4 (15 points)
**Multiple Choice**

Why does LSTM handle non-linear patterns better than ARIMA?

A) LSTM uses more historical data points  
B) LSTM has memory cells that can learn complex temporal dependencies  
C) LSTM automatically differences the data  
D) LSTM is a statistical model while ARIMA is machine learning  

---

## Question 5 (20 points)
**Code Snippet**

Write Python code to compute RMSE (Root Mean Squared Error) for forecast evaluation.

```python
# Your code here:
import numpy as np

def calculate_rmse(actual, predicted):
    """Calculate Root Mean Squared Error"""
    return np.sqrt(np.mean((actual - predicted) ** 2))

# Alternative using sklearn:
# from sklearn.metrics import mean_squared_error
# rmse = np.sqrt(mean_squared_error(actual, predicted))
```

---

## Question 6 (20 points)
**Short Answer**

When is differencing used in time series analysis, and what does it achieve? Provide a specific example from financial data.

*Write your answer in the space below (4-5 sentences expected):*

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---

## Answer Key

*The following section contains answers and is typically removed for student distribution.*

### Answers:

1. **B** - Stationarity of the time series
   - *Explanation:* The ADF test checks the null hypothesis that a time series has a unit root (is non-stationary). If p-value < 0.05, we reject the null and conclude the series is stationary.

2. **C** - The Autoregressive (AR) component with parameter p
   - *Explanation:* The AR(p) component captures how current values depend on p previous values, representing the autocorrelation structure. MA captures error correlations, and I handles non-stationarity.

3. **B** - Prophet automatically handles seasonality and missing data
   - *Explanation:* Prophet's key advantage is its robust handling of seasonal patterns, holidays, and missing values without manual preprocessing, making it more practical for business forecasting.

4. **B** - LSTM has memory cells that can learn complex temporal dependencies
   - *Explanation:* LSTM's architecture with forget, input, and output gates allows it to selectively remember and forget information, enabling capture of non-linear and long-term dependencies that ARIMA cannot model.

5. **Code Answer:**
   ```python
   import numpy as np
   
   def calculate_rmse(actual, predicted):
       """Calculate Root Mean Squared Error"""
       return np.sqrt(np.mean((actual - predicted) ** 2))
   
   # Alternative using sklearn:
   # from sklearn.metrics import mean_squared_error
   # rmse = np.sqrt(mean_squared_error(actual, predicted))
   ```

6. **Short Answer Expected Response:**
   Differencing is used when a time series is non-stationary, meaning its statistical properties (mean, variance) change over time. It transforms the data by computing the difference between consecutive observations to achieve stationarity. For example, stock prices are typically non-stationary with upward trends, but daily returns (first differences) are often stationary. First differencing: returns = price(t) - price(t-1). This transformation removes trends and makes the series suitable for ARIMA modeling, as most time series models assume stationarity.

---

*End of Quiz*