import pandas as pd

def transformCustomersData(df):
    #Remove duplicates
    df =df.drop_duplicates()

    #Handle Null Emails
    df =df.dropna(subset=["email"])

    #Standardize Names
    df["first_name"]=df["first_name"].str.title()
    df["last_name"]=df["last_name"].str.title()

    #Convert DateTime
    # 1. Convert the column to actual datetime objects
    df["created_date"]=pd.to_datetime(df["created_date"])
    df["updated_date"]=pd.to_datetime(df["updated_date"])
    # 2. Now you can safely convert it for MySQL
    df["created_date"] = df["created_date"].dt.to_pydatetime()
    df["updated_date"] = df["updated_date"].dt.to_pydatetime()

    return df

def transformProductsData(df):
    #Remove duplicates
    df =df.drop_duplicates()

    #Remove Invalid Prices
    df=df[df['price'] > 0]
    
    #Standardize Categories
    df["category"]=df["category"].str.title()

    return df

def transformOrdersData(df):
    """ #Remove duplicates
    df =df.drop_duplicates()

    #Convert DateTime
    
    # 1. Convert the column to actual datetime objects
    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date;
    print(df["order_date"])
    # 2. Now you can safely convert it for MySQL
    #df["order_date"] = df["order_date"].dt.to_pydatetime()

    #Remove Invalid Amount
    df=df[df['amount'] > 0]

    #Add New columns Year&Month of Orders
    df["order_year"]=int(df["order_date"].dt.year)
    df["order_month"]=int(df["order_date"].dt.month)
    
    return df """
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # convert order_date
    df['order_date'] = pd.to_datetime(df['order_date'])
    # Add orders month
    #print(df['order_date'])
    df['order_month'] = df['order_date'].dt.month

    # Add order Year
    df['order_year'] = df['order_date'].dt.year
    # 2. Now you can safely convert it for MySQL
    df['order_date'] = df['order_date'].dt.to_pydatetime()
    

    
    # remove invalid amounts
    df = df[df['amount'] > 0]

    
    
    # Select final columns
    """
    
    df = df[
        [
            "order_id",
            "customer_id",
            "order_date",
            "amount"
        ]
    ]
    print(df)
    """
    return df
    
def transformSalesData(df):
    #Remove duplicates
    df =df.drop_duplicates()

    #Invalid Quantites
    df=df[df['quantity'] > 0]

    #Remove Invalid Sale Amount
    df=df[df['sale_amount'] > 0]

    #Convert DateTime
    # 1. Convert the column to actual datetime objects
    df["last_updated"]=pd.to_datetime(df["last_updated"])
    # 2. Now you can safely convert it for MySQL
    df["last_updated"] = df["last_updated"].dt.to_pydatetime()

    #High Value Flag
    df["high_value_sale"]= df['sale_amount'] > 1000

    return df

    