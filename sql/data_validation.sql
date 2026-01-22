SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM transactions;

SELECT COUNT(*) 
FROM transactions
WHERE transaction_amount <= 0;

SELECT COUNT(*) 
FROM transactions
WHERE transaction_status IS NULL;
