CREATE TABLE IF NOT EXISTS fact_sales (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    category VARCHAR(100),
    quantity INT,
    price FLOAT,
    total_amount FLOAT,
    order_date DATE
);
