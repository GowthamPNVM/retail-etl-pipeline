import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime,timedelta

fake = Faker() #intilize fake instance
random.seed(42) # sets seed for random module
np.random.seed(42) #sets sed for numpy module

def genearte_customers(num_customers=10000):
    #"Genearete the customers data"
    customers = []

    for customers_id in range(1,num_customers+1):
        customers.append({
            "customer_id":customers_id,
            "first_name":fake.first_name(),
            "last_name":fake.last_name(),
            "email":fake.unique.email(),
            "city":fake.city(),
            "state":fake.state(),
            "country":fake.country(),
            "created_date":fake.date_between(start_date='-2y',end_date="today"),
            "created_by":'ADMIN',
            "updated_date":datetime.now(),
            "updated_by":'ADMIN',
	        "active_status":'1'
        });
    return pd.DataFrame(customers);

def genearte_products(num_products=1000):
    categories=["Electronics","Clothing","Home & Kitchen","Beauty","Books","Sports","Toys"]
    #"Genearete the products data"
    products = []
    for product_id in range(1,num_products+1):
        products.append({
            "product_id":product_id,
            "product_name":fake.word().capitalize(),
            "category":random.choice(categories),
            "price":round(random.uniform(10,1000),2),
            "added_date":datetime.now(),
            "added_by":'ADMIN'
        })
    return pd.DataFrame(products);

def genearte_orders(num_orders=100000,num_customers=100000):
    #genearte random orders for the customers
    orders = []
    for order_id in range(1,num_orders+1):
        orders.append({
            "order_id":order_id,
            "customer_id":np.random.randint(1,num_customers),
	        "order_date":fake.date_between(start_date='-2y',end_date="today"),
            "amount":round(random.uniform(10,1000),2),
            "added_date":datetime.now(),
            "added_by":'ADMIN'
        })
    return pd.DataFrame(orders);
"""
def genearte_sales(orders_df_num_products=1000,num_sales=500000):
    sales = []
    for sales_id in range(1,num_sales+1):
        orders = orders_df.sample(1).iloc[0]
        quanity= np.random.randint(1,10)
        sales_amount = round(random.uniform(20,2000),2)
        sales.append({
            "sale_id":sales_id,
            "order_id":orders["order_id"],
            "product_id":np.random.randint(1,1000),
            "quantity":quanity,
            "sale_amount":sales_amount,
            "last_updated":datetime.now()
        }) 
    return pd.DataFrame(sales)
"""
def generate_sales(orders_df, num_sales=500000, num_products=1000):

    sales = []

    # Convert order_ids once
    order_ids = orders_df["order_id"].tolist()

    for sale_id in range(1, num_sales + 1):

        sales.append({
            "sale_id": sale_id,
            "order_id": random.choice(order_ids),
            "product_id": np.random.randint(1, num_products + 1),
            "quantity": np.random.randint(1, 10),
            "sale_amount": round(random.uniform(20, 2000), 2),
            "last_updated": datetime.now()
        })

    return pd.DataFrame(sales)

if __name__ == "__main__":
    print("genearte_customers")
    customers_df = genearte_customers()

    print("genearte_products")
    products_df = genearte_products()

    print("genearte_orders")
    orders_df = genearte_orders()

    print("genearte sales")
    sales_df = generate_sales(orders_df)

    print("Data geneartion completed succesfully")

    print("export CSV file")
    customers_df.to_csv("data/raw/customers.csv",index=False)
    products_df.to_csv("data/raw/products.csv",index=False)
    orders_df.to_csv("data/raw/orders.csv",index=False)
    sales_df.to_csv("data/raw/sales.csv",index=False)

    print("Data exported Succesfully")

    
    