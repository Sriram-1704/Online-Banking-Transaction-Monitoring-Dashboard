import pandas as pd
import os

# Loading Processed Data
customers_df = pd.read_csv("data/processed/customers_processed.csv")
transactions_df = pd.read_csv("data/processed/transactions_processed.csv")

print("Processed data loaded")
print(customers_df.shape)
print(transactions_df.shape)

# Converting date column into datetime format
transactions_df['transaction_date'] = pd.to_datetime(
    transactions_df['transaction_date']
)

transactions_df['year'] = transactions_df['transaction_date'].dt.year
transactions_df['month'] = transactions_df['transaction_date'].dt.month
transactions_df['month_name'] = transactions_df['transaction_date'].dt.month_name()
transactions_df['day'] = transactions_df['transaction_date'].dt.day
transactions_df['day_name'] = transactions_df['transaction_date'].dt.day_name()
transactions_df['week'] = transactions_df['transaction_date'].dt.isocalendar().week

# High-Risk Transaction
high_value_threshold = 50000

transactions_df['high_value_flag'] = transactions_df['transaction_amount'] > high_value_threshold

# Calculating average transaction amount per customer
customer_avg_txn = (
    transactions_df
    .groupby('customer_id')['transaction_amount']
    .mean()
    .reset_index(name='customer_avg_transaction')
)

# Joining customer-level metrics back to transactions
transactions_df = transactions_df.merge(
    customer_avg_txn,
    on='customer_id',
    how='left'
)

# Suspicious Transaction Detection 
transactions_df['suspicious_flag'] = (
    (transactions_df['transaction_amount'] > transactions_df['customer_avg_transaction'] * 3) |
    (transactions_df['high_value_flag'])
)

# Counting number of transactions per customer per day
txn_frequency = (
    transactions_df
    .groupby(['customer_id', 'transaction_date'])
    .size()
    .reset_index(name='daily_txn_count')
)

transactions_df = transactions_df.merge(
    txn_frequency,
    on=['customer_id', 'transaction_date'],
    how='left'
)

transactions_df['high_frequency_flag'] = transactions_df['daily_txn_count'] > 5

# Default Risk Indicator
transactions_df['risk_level'] = 'Low'

# Assigning High Risk 
transactions_df.loc[
    transactions_df['suspicious_flag'] | transactions_df['high_frequency_flag'],
    'risk_level'
] = 'High'

# Saving Analytical Data
os.makedirs("data/analytics", exist_ok=True)

customers_df.to_csv(
    "data/analytics/customers_analytics.csv",
    index=False
)

transactions_df.to_csv(
    "data/analytics/transactions_analytics.csv",
    index=False
)

print("Analysis completed successfully")

