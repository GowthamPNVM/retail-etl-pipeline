CREATE DATABASE IF NOT EXISTS Retail_ETL;
USE Retail_ETL;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS sales;
CREATE TABLE IF NOT EXISTS customers(
    customer_id INT(11) Primary key AUTO_INCREMENT,
    first_name varchar(100) NOT NULL,
    last_name varchar(100),
    email varchar(50) UNIQUE,
    city varchar(50),
    state varchar(50),
    country varchar(50),
    created_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by varchar(100) NOT NULL DEFAULT 'ADMIN',
    updated_date  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by varchar(100) NOT NULL DEFAULT 'ADMIN',
	active_status tinyint (1) NOT NULL DEFAULT 1
); 
CREATE TABLE IF NOT EXISTS products(
    product_id int(11) Primary key AUTO_INCREMENT,
    product_name varchar(50) NOT NULL,
    category varchar(25),
    price decimal(20,6) NOT NULL
);
 CREATE TABLE IF NOT EXISTS orders(
    order_id int(11) primary key AUTO_INCREMENT,
    customer_id int(11),
	order_date date NOT NULL,
    amount float(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS sales(
    sale_id int(11) Primary key AUTO_INCREMENT,
    order_id int(11) NOT NULL,
    product_id int(11) NOT NULL,
    quantity int(11) NOT NULL,
    sale_amount float(10) NOT NULL,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
)

create table IF NOT EXISTS retail_etl.etl_metadata(
							#metadata_id INT(11) Primary key AUTO_INCREMENT,
                            table_name VARCHAR(100) primary key,
                            last_loaded_date datetime);

ALTER TABLE products ADD added_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
		ALTER TABLE products ADD added_by  varchar(100) NOT NULL DEFAULT 'ADMIN';
		ALTER TABLE orders ADD added_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
		ALTER TABLE orders ADD added_by  varchar(100) NOT NULL DEFAULT 'ADMIN';