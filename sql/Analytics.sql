USE retail_etl;
#Total Revenue 
SELECT  round(sum(sales.sale_amount),2) as total_revenue FROM retail_etl.sales;

#Monthly Revenue Trend
SELECT orders.order_year,MONTHNAME(STR_TO_DATE(orders.order_month, '%m')) AS month_name,orders.order_month,round(sum(sales.sale_amount),2) as monthly_revenue  FROM orders JOIN sales ON sales.order_id = orders.order_id GROUP BY 1,2 ORDER BY 1 DESC, 3 DESC;

#Top ten customers
SELECT customers.customer_id,concat(customers.first_name,' ',customers.last_name) as customer_name,round(sum(orders.amount),2) as spend_amount
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id  
ORDER BY spend_amount DESC LIMIT 0,10;

#Top selling products 
SELECT products.product_id,products.product_name,SUM(sales.quantity) as sell_count
FROM products
JOIN sales ON sales.product_id = products.product_id
GROUP BY products.product_id
ORDER BY 3 DESC; 

#High Values Sales Percentage
SELECT sales.high_value_sale,ROUND(SUM(sales.high_value_sale)/COUNT(*)*100,2)  as HIGH_VAL_PERC
FROM sales ;

#CUSTOMER Order Frequency
SELECT customers.customer_id,concat(customers.first_name,' ',customers.last_name) as customer_name,COUNT(orders.order_id) as order_count
FROM customers
JOIN orders ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id  
ORDER BY order_count DESC;