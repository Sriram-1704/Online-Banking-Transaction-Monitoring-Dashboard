import pandas as pd
import mysql.connector
import os

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",                
    password="1234",   
    database="online_banking_db"
)


# Load Data from MySQL
customers_df = pd.read_sql("SELECT * FROM customers", conn)
transactions_df = pd.read_sql("SELECT * FROM transactions", conn)

conn.close()

print("Data loaded successfully")
print("Customers shape:", customers_df.shape)
print("Transactions shape:", transactions_df.shape)
print(customers_df.info())
print(transactions_df.info())

# Checking missing values
print(customers_df.isnull().sum())
print(transactions_df.isnull().sum())

# Fixing Data Type 
transactions_df['transaction_date'] = pd.to_datetime(
    transactions_df['transaction_date']
)

# Removing Duplicates
customers_df.drop_duplicates(inplace=True)
transactions_df.drop_duplicates(inplace=True)

# Handling Missing Values
customers_df['city'].fillna('Unknown', inplace=True)
customers_df['account_type'].fillna('Unknown', inplace=True)

transactions_df['transaction_status'].fillna('Unknown', inplace=True)
transactions_df['merchant_category'].fillna('Unknown', inplace=True)
transactions_df['location'].fillna('Unknown', inplace=True)

# Standardizing Text Columns
customers_df['city'] = customers_df['city'].str.title()
customers_df['account_type'] = customers_df['account_type'].str.title()

transactions_df['transaction_type'] = transactions_df['transaction_type'].str.title()
transactions_df['merchant_category'] = transactions_df['merchant_category'].str.title()
transactions_df['location'] = transactions_df['location'].str.title()
transactions_df['transaction_status'] = transactions_df['transaction_status'].str.title()

# Validating the data
print(customers_df.describe(include='all'))
print(transactions_df.describe())

# Saving Cleaned Data
os.makedirs("data/processed", exist_ok=True)

customers_df.to_csv(
    "data/processed/customers_processed.csv",
    index=False
)

transactions_df.to_csv(
    "data/processed/transactions_processed.csv",
    index=False
)

