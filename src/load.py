import pandas as pd
import mysql.connector
from utils import read_config

def createConnection():
    try:
        config = read_config()
        conn = mysql.connector.connect(
                                        host=config["mysql"]["host"],
                                        user=config["mysql"]["user"],
                                        password=config["mysql"]["password"],
                                        database=config["mysql"]["database"]
                                    )
        return conn;
    except Exception as e:
        print(f"Connection Error {str(e)}")
        
"""Load the data into MySQL Database"""
"""
def load_data(df,tableName,connection):    
        cursor = connection.cursor()
        
        try:    
            columns= ",".join(df.columns)       
            
            placeholders = ",".join(["%s"]*len(df.columns))
            
            #insert Query
            insertQry = f"Insert INTO {tableName} ({columns}) values ({placeholders})"
            
            print(insertQry)
            
            #Database Friendly Tuples
            data = list(df.itertuples(index=False,name=None))
            cursor.executemany(insertQry,data)        
            connection.commit()
            print(f"Load Sucessfully {tableName}")
        except Exception as e:
            print(f"Exception raised for {tableName} of {str(e)}")
        finally:
            print(f"Cursor Closed Successfully")
            cursor.close()
"""
"""Enhanced load_data function with:batch processing, dynamic datetime handling, and connection health checks"""

def load_data(df, tableName, connection, batch_size=2000):    
    # 1. Health Check: Reconnect if the connection dropped before this table started
    if not connection.is_connected():
        print(f"Connection lost before loading {tableName}. Reconnecting...")
        connection.reconnect(attempts=3, delay=2)
        
    cursor = connection.cursor()
    
    try:    
        # 2. Dynamic Query Generation
        columns = ",".join(df.columns)       
        placeholders = ",".join(["%s"] * len(df.columns))
        insertQry = f"INSERT INTO {tableName} ({columns}) VALUES ({placeholders})"
        print(insertQry)
        
        # 3. Dynamic Datetime Formatting
        # Automatically finds and converts any timestamp/datetime columns to strings
        df_clean = df.copy()
        for col in df_clean.columns:
            if pd.api.types.is_datetime64_any_dtype(df_clean[col]):
                df_clean[col] = df_clean[col].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert to database-friendly tuples
        data = list(df_clean.itertuples(index=False, name=None))
        
        # 4. Chunked Batch Insertion to prevent Error 10054
        total_rows = len(data)
        print(f"Starting load for {tableName}: {total_rows} total rows.")
        
        for i in range(0, total_rows, batch_size):
            chunk = data[i : i + batch_size]
            cursor.executemany(insertQry, chunk)
            connection.commit()  # Save progress per batch
            
        print(f"Load Successfully {tableName}")
        
    except Exception as e:
        connection.rollback()  # Undo the current failed chunk if an error occurs
        print(f"Exception raised for {tableName} of {str(e)}")
    finally:
        print(f"Cursor Closed Successfully")
        cursor.close()
