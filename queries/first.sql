SELECT COUNT(*) FROM orders;
SELECT * FROM orders LIMIT 5;
SELECT order_status, COUNT(*) FROM orders GROUP BY order_status;
SELECT COUNT(*) FROM customers;
SELECT customer_state, COUNT(*) AS n FROM customers GROUP BY customer_state ORDER BY n DESC LIMIT 5;
