from extract import extract_csv
from utils import setup_logger

logger =setup_logger()

def main():
    try:
        print("ETL Pipeline Started")
        logger.info(f"ETL Pipeline Started")
        customers_df = extract_csv("data/raw/customers.csv",["customer_id","first_name","last_name","email"])
        logger.info(f"Customers Data Piped :{len(customers_df)} rows")
        products_df = extract_csv("data/raw/products.csv",["product_id","product_name","category","price"])
        logger.info(f"Products Data Piped :{len(products_df)} rows")
        orders_df = extract_csv("data/raw/orders.csv",["order_id","customer_id","order_date","amount"])
        logger.info(f"Orders Data Piped :{len(orders_df)} rows")
        sales_df = extract_csv("data/raw/sales.csv",["sale_id","order_id","product_id","quantity","sale_amount"])
        logger.info(f"Sales Data Piped :{len(sales_df )} rows")
        logger.info("Data Pipeline Ended")
        print("Data Pipeline Ended")
    except Exception as e:
        logger.error(f"Error {str(e)} ")

if __name__== "__main__":
    main()