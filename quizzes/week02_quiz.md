---
title: "Week 2 Quiz — Data Wrangling & Feature Engineering for Finance"
week: 2
author: "Praveen Kumar"
date: 2025-10-07
duration: "35 minutes"
total_points: 100
version: v1.0
---

# Week 2 Quiz — Data Wrangling & Feature Engineering for Finance

**Instructions:** Complete all questions within the time limit. Show your work for calculations and provide clear explanations for short answer questions.

**Time Limit:** 35 minutes  
**Total Points:** 100

---

## Question 1 (15 points)
**Multiple Choice**

What is a log return, and why is it preferred over simple returns in financial modeling?

A) Log returns are easier to calculate and require less computational power  
B) Log returns are normally distributed and additive over time, making them ideal for statistical modeling  
C) Log returns always produce positive values, avoiding negative return issues  
D) Log returns eliminate the need for data preprocessing and outlier treatment  

---

## Question 2 (15 points)
**Multiple Choice**

Which technique is most effective for detecting multicollinearity among financial features?

A) Correlation coefficient analysis only  
B) Variance Inflation Factor (VIF) analysis  
C) Principal Component Analysis loadings  
D) Random Forest feature importance scores  

---

## Question 3 (15 points)
**Multiple Choice**

What is the primary advantage of Principal Component Analysis (PCA) in financial feature engineering?

A) It automatically selects the most profitable trading signals  
B) It reduces dimensionality while preserving maximum variance and eliminates multicollinearity  
C) It converts all features to the same scale without information loss  
D) It removes outliers and missing values from the dataset  

---

## Question 4 (15 points)
**Multiple Choice**

When calculating the Relative Strength Index (RSI), what does an RSI value above 70 typically indicate?

A) The stock is undervalued and should be bought immediately  
B) The stock has high volatility and requires hedging  
C) The stock may be overbought and due for a price correction  
D) The stock has strong fundamental performance  

---

## Question 5 (20 points)
**Short Answer**

Explain the importance of feature scaling in financial machine learning and describe two scenarios where improper scaling could lead to model failure.

*Write your answer in the space below (4-5 sentences expected):*

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---

## Question 6 (20 points)
**Code Snippet**

Write a Python code snippet using pandas to calculate 10-day rolling volatility (standard deviation) of daily returns, annualized by multiplying by √252. Assume 'prices' is a pandas Series.

```python
# Your code here:




```

---

## Answer Key

*The following section contains answers and is typically removed for student distribution.*

### Answers:

1. **B** - Log returns are normally distributed and additive over time, making them ideal for statistical modeling
   - *Explanation:* Log returns have mathematical advantages including approximate normality, time additivity, and symmetry around zero, making them superior for statistical modeling.

2. **B** - Variance Inflation Factor (VIF) analysis
   - *Explanation:* VIF specifically measures multicollinearity by quantifying how much coefficient variance increases due to collinearity. VIF > 10 indicates problematic multicollinearity.

3. **B** - It reduces dimensionality while preserving maximum variance and eliminates multicollinearity
   - *Explanation:* PCA's main benefit is creating orthogonal components that capture maximum variance in fewer dimensions while eliminating multicollinearity issues.

4. **C** - The stock may be overbought and due for a price correction
   - *Explanation:* RSI > 70 traditionally indicates overbought conditions, suggesting potential for price pullback, though it should be used with other indicators.

5. **Short Answer Expected Response:**
   Feature scaling is crucial because financial features have vastly different scales (prices vs returns vs ratios). Two failure scenarios: (1) In PCA, unscaled features with larger magnitudes dominate the analysis, causing less important high-scale features to overshadow predictive patterns. (2) In distance-based algorithms, unscaled features create misleading distance calculations where high-magnitude features overwhelm important low-magnitude features, leading to poor model performance.

6. **Code Answer:**
   ```python
   returns = prices.pct_change()
   volatility_10d = returns.rolling(10).std() * np.sqrt(252)
   ```

---

*End of Quiz*