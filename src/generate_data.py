import pandas as pd
import numpy as np
import os

np.random.seed(42)

os.makedirs("data/raw", exist_ok=True)

num_customers = 500
num_transactions = 5000

customer_ids = np.arange(1, num_customers + 1)

ages = np.random.randint(18, 71, num_customers)
incomes = np.random.randint(30000, 150001, num_customers).astype(float)

missing_count = int(0.05 * num_customers)
missing_indexes = np.random.choice(num_customers, missing_count, replace=False)
incomes[missing_indexes] = np.nan

signup_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2023-01-01", "2026-01-01"),
        num_customers
    )
)

demographics = pd.DataFrame({
    "customer_id": customer_ids,
    "age": ages,
    "income": incomes,
    "signup_date": signup_dates
})

transaction_ids = np.arange(1, num_transactions + 1)

transaction_customer_ids = np.random.choice(customer_ids, num_transactions)

transaction_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2024-01-01", "2026-06-01"),
        num_transactions
    )
)

amounts = np.random.exponential(scale=120, size=num_transactions)

outlier_count = int(0.02 * num_transactions)
outlier_indexes = np.random.choice(num_transactions, outlier_count, replace=False)
amounts[outlier_indexes] *= 20

negative_count = int(0.01 * num_transactions)
negative_indexes = np.random.choice(num_transactions, negative_count, replace=False)
amounts[negative_indexes] *= -1

categories = np.random.choice(
    ["Electronics", "Clothing", "Home"],
    num_transactions
)

transactions = pd.DataFrame({
    "transaction_id": transaction_ids,
    "customer_id": transaction_customer_ids,
    "transaction_date": transaction_dates,
    "amount": amounts,
    "category": categories
})

demographics.to_csv("data/raw/demographics.csv", index=False)
transactions.to_csv("data/raw/transactions.csv", index=False)

print("Files generated successfully")
print("demographics.csv created")
print("transactions.csv created")