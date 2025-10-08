import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic credit scoring dataset
n_samples = 10000

# Generate features
age = np.random.randint(18, 80, n_samples)
income = np.random.exponential(50000, n_samples)
employment_length = np.random.randint(0, 30, n_samples)
debt_to_income = np.random.beta(2, 5, n_samples)
credit_history_length = np.random.randint(0, 40, n_samples)
num_credit_accounts = np.random.poisson(3, n_samples)
recent_inquiries = np.random.poisson(1, n_samples)
loan_amount = np.random.exponential(25000, n_samples)

# Categorical features
home_ownership = np.random.choice(['rent', 'own', 'mortgage'], n_samples, p=[0.4, 0.3, 0.3])
employment_type = np.random.choice(['full_time', 'part_time', 'self_employed', 'unemployed'], n_samples, p=[0.6, 0.2, 0.15, 0.05])
loan_purpose = np.random.choice(['debt_consolidation', 'home_improvement', 'business', 'other'], n_samples, p=[0.4, 0.3, 0.2, 0.1])

# Create target based on realistic risk factors
risk_score = (
    -0.02 * age +
    -0.00001 * income +
    -0.01 * employment_length +
    2.0 * debt_to_income +
    -0.01 * credit_history_length +
    0.1 * num_credit_accounts +
    0.3 * recent_inquiries +
    0.00001 * loan_amount +
    np.random.normal(0, 0.5, n_samples)
)

# Convert to probability and then to binary target
prob_default = 1 / (1 + np.exp(-risk_score))
target = (prob_default > 0.3).astype(int)  # About 30% default rate

# Create DataFrame
df = pd.DataFrame({
    'age': age,
    'income': income,
    'employment_length': employment_length,
    'debt_to_income': debt_to_income,
    'credit_history_length': credit_history_length,
    'num_credit_accounts': num_credit_accounts,
    'recent_inquiries': recent_inquiries,
    'loan_amount': loan_amount,
    'home_ownership': home_ownership,
    'employment_type': employment_type,
    'loan_purpose': loan_purpose,
    'target': target
})

# Save to CSV
df.to_csv('data/synthetic/credit_scoring.csv', index=False)
print(f'Generated synthetic credit scoring dataset: {len(df)} samples')
print(f'Default rate: {target.mean():.2%}')
print(f'Features: {list(df.columns)}')