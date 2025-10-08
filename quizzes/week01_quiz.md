---
title: "Week 1 Quiz — Introduction to Financial ML & Linear Regression"
week: 1
author: "Praveen Kumar"
date: 2025-10-07
duration: "30 minutes"
total_points: 100
version: v1.0
---

# Week 1 Quiz — Introduction to Financial ML & Linear Regression

**Instructions:** Complete all questions. For multiple choice, select the best answer. Show your work for short answer and code questions.

**Time Limit:** 30 minutes  
**Total Points:** 100

---

## Question 1 (15 points)
**Multiple Choice**

Which metric is best suited to evaluate the performance of continuous regression models in financial applications?

A) Accuracy  
B) Mean Squared Error (MSE)  
C) ROC-AUC  
D) F1-Score  

---

## Question 2 (15 points)
**Multiple Choice**

What does 'lag' refer to in the context of time-series feature engineering for financial data?

A) The delay in data availability from market sources  
B) Previous time period values used as input features  
C) The time it takes for a model to make predictions  
D) The difference between predicted and actual values  

---

## Question 3 (15 points)
**Multiple Choice**

Why is chronological splitting (instead of random splitting) crucial when working with financial time series data?

A) It makes the model train faster  
B) It ensures better statistical distribution  
C) It prevents data leakage and look-ahead bias  
D) It improves the R² score automatically  

---

## Question 4 (15 points)
**Multiple Choice**

In financial machine learning, what is the primary purpose of standardizing features before training a linear regression model?

A) To make the data normally distributed  
B) To ensure all features contribute equally to the model regardless of their original scale  
C) To remove outliers from the dataset  
D) To increase the R² score of the model  

---

## Question 5 (20 points)
**Short Answer**

Explain why we split time series data chronologically rather than randomly, and what problems could arise if we used random splits in financial modeling.

*Write your answer in the space below (3-4 sentences expected):*

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

___________________________________________________________________

---

## Question 6 (20 points)
**Code Snippet**

Write a one-line Python code snippet using scikit-learn that fits a LinearRegression model on training data (X_train, y_train) and then makes predictions on test data (X_test). Store the predictions in a variable called 'predictions'.

```python
# Your code here:

```

---

## Answer Key

*The following section contains answers and is typically removed for student distribution.*

### Answers:

1. **B** - Mean Squared Error (MSE)
   - *Explanation:* MSE measures the average squared differences between predicted and actual values, making it appropriate for continuous variables like stock returns.

2. **B** - Previous time period values used as input features
   - *Explanation:* Lag features use historical values (e.g., yesterday's return) as input variables to predict current or future outcomes.

3. **C** - It prevents data leakage and look-ahead bias
   - *Explanation:* Chronological splitting ensures that the model only uses past information to predict future outcomes, preventing unrealistic performance estimates.

4. **B** - To ensure all features contribute equally to the model regardless of their original scale
   - *Explanation:* Standardization ensures that features with different scales don't dominate the model due to their magnitude.

5. **Short Answer Expected Response:**
   Chronological splitting preserves temporal order, ensuring we only use past information to predict future outcomes. Random splitting causes data leakage by allowing future information to influence predictions about the past, leading to unrealistically high performance that doesn't reflect real-world conditions.

6. **Code Answer:**
   ```python
   predictions = LinearRegression().fit(X_train, y_train).predict(X_test)
   ```

---

*End of Quiz*