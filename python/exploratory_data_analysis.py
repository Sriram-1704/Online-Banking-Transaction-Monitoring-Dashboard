import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Analytics Data
transactions_df = pd.read_csv(
    "data/analytics/transactions_analytics.csv"
)

print(transactions_df.shape)

# Calculating Columns
total_transactions = len(transactions_df)
total_amount = transactions_df['transaction_amount'].sum()
avg_transaction = transactions_df['transaction_amount'].mean()
high_risk_count = transactions_df[transactions_df['risk_level'] == 'High'].shape[0]

print("Total Transactions:", total_transactions)
print("Total Transaction Amount:", round(total_amount, 2))
print("Average Transaction Amount:", round(avg_transaction, 2))
print("High Risk Transactions:", high_risk_count)

# Transaction Amount Distribution
plt.figure()
sns.histplot(transactions_df['transaction_amount'], bins=50)
plt.title("Transaction Amount Distribution")
plt.xlabel("Transaction Amount")
plt.ylabel("Count")
plt.savefig("images/transaction_amount_distribution.png", bbox_inches="tight")
plt.show()

# Transactions by Type
plt.figure()
sns.countplot(
    data=transactions_df,
    x='transaction_type'
)
plt.title("Transaction Count by Type")
plt.xlabel("Transaction Type")
plt.ylabel("Count")
plt.savefig("images/transactions_by_type.png", bbox_inches="tight")
plt.show()

# Monthly Transaction Trend
monthly_trend = (
    transactions_df
    .groupby('month_name')['transaction_amount']
    .sum()
    .reindex([
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ])
)

plt.figure()
monthly_trend.plot(kind='line')
plt.title("Monthly Transaction Amount Trend")
plt.xlabel("Month")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.savefig("images/monthly_transaction_trend.png", bbox_inches="tight")
plt.show()

# Merchant Category Analysis
plt.figure()
sns.barplot(
    data=transactions_df,
    x='merchant_category',
    y='transaction_amount',
    estimator=sum
)
plt.title("Transaction Amount by Merchant Category")
plt.xlabel("Merchant Category")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.savefig("images/merchant_category_analysis.png", bbox_inches="tight")
plt.show()

# Risk Level Distribution
plt.figure()
sns.countplot(
    data=transactions_df,
    x='risk_level'
)
plt.title("Risk Level Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.savefig("images/risk_level_distribution.png", bbox_inches="tight")
plt.show()

# High-Risk Transactions by Month
high_risk_monthly = (
    transactions_df[transactions_df['risk_level'] == 'High']
    .groupby('month_name')
    .size()
    .reindex([
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ])
)

plt.figure()
high_risk_monthly.plot(kind='bar')
plt.title("High-Risk Transactions by Month")
plt.xlabel("Month")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("images/high_risk_transactions_by_month.png", bbox_inches="tight")
plt.show()

print("EDA completed successfully")
