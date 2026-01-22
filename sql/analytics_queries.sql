-- Monthly transaction amount
SELECT 
    MONTH(transaction_date) AS month,
    SUM(transaction_amount) AS total_amount
FROM transactions
GROUP BY month;

-- High-risk transactions
SELECT COUNT(*) 
FROM transactions
WHERE transaction_amount > 10000;

-- Transactions by merchant category
SELECT merchant_category, SUM(transaction_amount)
FROM transactions
GROUP BY merchant_category;
