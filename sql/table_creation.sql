CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    location VARCHAR(50),
    account_type VARCHAR(50),
    account_open_date DATE
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    transaction_date DATE,
    transaction_amount DECIMAL(12,2),
    transaction_type VARCHAR(20),
    merchant_category VARCHAR(50),
    transaction_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
