-- Monthly Revenue
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(total_amount) AS revenue
FROM fact_sales
GROUP BY month
ORDER BY month;

-- Top Selling Product
SELECT product, SUM(quantity) as total_sold
FROM fact_sales
GROUP BY product
ORDER BY total_sold DESC;

-- Revenue by Category
SELECT category, SUM(total_amount) as revenue
FROM fact_sales
GROUP BY category;
