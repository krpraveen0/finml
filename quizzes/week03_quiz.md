---
title: "Week 3 Quiz — Supervised ML in Finance"
week: 3
author: "Praveen Kumar"
date: 2025-10-07
duration: "35 minutes"
total_points: 100
version: v1.0
---

# Week 3 Quiz — Supervised ML in Finance

**Instructions:** Answer all questions. Show your work for code and short answers.

---

## Question 1 (15 points)
**Multiple Choice**

Which metric is most appropriate for evaluating imbalanced classification problems?

A) Accuracy  
B) Precision  
C) F1 Score  
D) ROC-AUC

---

## Question 2 (15 points)
**Multiple Choice**

What is the decision boundary in Logistic Regression?

A) The point where predicted probability equals 0.5  
B) The value of the largest coefficient  
C) The mean of all features  
D) The maximum predicted probability

---

## Question 3 (15 points)
**Multiple Choice**

Why is Random Forest less prone to overfitting than a single Decision Tree?

A) It uses regularization  
B) It averages predictions from many trees trained on bootstrapped samples  
C) It only uses the most important features  
D) It prunes branches aggressively

---

## Question 4 (15 points)
**Multiple Choice**

What does the confusion matrix represent in classification?

A) The distribution of feature importances  
B) The breakdown of true/false positives and negatives  
C) The ROC curve  
D) The model's hyperparameters

---

## Question 5 (20 points)
**Code Snippet**

Write sklearn code to compute the ROC-AUC score for a binary classifier.

```python
# Your code here:
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_true, y_pred_proba)
```

---

## Question 6 (20 points)
**Short Answer**

Explain the business interpretation of a model with high recall but low precision in credit scoring.

*Write your answer below (3-4 sentences expected):*

---

## Answer Key

1. **D** — ROC-AUC. It measures discrimination and is robust to class imbalance.
2. **A** — The point where predicted probability equals 0.5.
3. **B** — It averages predictions from many trees trained on bootstrapped samples.
4. **B** — The breakdown of true/false positives and negatives.
5. **Code:**
```python
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_true, y_pred_proba)
```
6. **Short Answer:**
High recall means most actual defaulters are identified, reducing missed risks. Low precision means many predicted defaulters are actually good applicants, leading to more false positives. In business, this reduces risk but may reject more good customers, impacting revenue and customer satisfaction. The trade-off must be managed based on business priorities.