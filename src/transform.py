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
    df["created_date"]=pd.to_datetime(df["created_date"])
    df["updated_date"]=pd.to_datetime(df["updated_date"])

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
    #Remove duplicates
    df =df.drop_duplicates()

    #Convert DateTime
    df["order_date"]=pd.to_datetime(df["order_date"])

    #Remove Invalid Amount
    df=df[df['amount'] > 0]

    #Add New columns Year&Month of Orders
    df["order_year"]=df["order_date"].dt.year
    df["order_month"]=df["order_date"].dt.month

    return df

def transformSalesData(df):
    #Remove duplicates
    df =df.drop_duplicates()

    #Invalid Quantites
    df=df[df['quantity'] > 0]

    #Remove Invalid Sale Amount
    df=df[df['sale_amount'] > 0]

    #Convert DateTime
    df["last_updated"]=pd.to_datetime(df["last_updated"])

    #High Value Flag
    df["high_value_sale"]= df['sale_amount'] > 1000

    return df

    