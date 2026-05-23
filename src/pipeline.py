from extract import extract_csv
from utils import setup_logger
from transform import transformCustomersData,transformOrdersData,transformProductsData,transformSalesData

logger =setup_logger()

def main():
    try:
        print("ETL Pipeline Started")
        logger.info(f"Extraction of Data Started")
        customers_df = extract_csv("data/raw/customers.csv",["customer_id","first_name","last_name","email"])
        logger.info(f"Customers Data Piped :{len(customers_df)} rows")
        products_df = extract_csv("data/raw/products.csv",["product_id","product_name","category","price"])
        logger.info(f"Products Data Piped :{len(products_df)} rows")
        orders_df = extract_csv("data/raw/orders.csv",["order_id","customer_id","order_date","amount"])
        logger.info(f"Orders Data Piped :{len(orders_df)} rows")
        sales_df = extract_csv("data/raw/sales.csv",["sale_id","order_id","product_id","quantity","sale_amount"])
        logger.info(f"Sales Data Piped :{len(sales_df )} rows")
        logger.info("Extraction of Data Ended")
        print("Transformation Data Started")
        logger.info(f"Transform Data Started")
        transformed_customers_df = transformCustomersData(customers_df)
        logger.info(f"Transformed Customers Data :{len(transformed_customers_df)} rows")
        transformed_products_df = transformProductsData(products_df)
        logger.info(f"Transformed Products Data :{len(transformed_products_df)} rows")
        transformed_orders_df = transformOrdersData(orders_df)
        logger.info(f"Transformed Orders Data :{len(transformed_orders_df)} rows")
        transform_sales_df = transformSalesData(sales_df)
        logger.info(f"Transformed Sales Data :{len(transform_sales_df )} rows")
        logger.info("Transform Data Ended")
        print("Transformation Data Ended")
        print("ETL Pipeline Ended")

    except Exception as e:
        logger.error(f"Error {str(e)} ")

if __name__== "__main__":
    main()