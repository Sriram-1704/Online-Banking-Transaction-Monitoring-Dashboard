import pandas as pd
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="1234",
    database="online_banking_db"
)

# Read tables into DataFrames
customers_df = pd.read_sql("SELECT * FROM customers", conn)
transactions_df = pd.read_sql("SELECT * FROM transactions", conn)

conn.close()

# Validating the data
print(customers_df.head())
print(transactions_df.head())

print(customers_df.shape)
print(transactions_df.shape)
