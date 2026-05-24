from datetime import datetime

""" Get the last loaded date for incremental load """
def get_last_loaded_date(tableName,connection):
    cursor = connection.cursor()
    try:
        query = f"SELECT last_loaded_date FROM etl_metadata WHERE table_name = '{tableName}'"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        #print(f"Error fetching last loaded date for {tableName}: {str(e)}")
        return None
    
""" Last loaded date for incremental load"""    
def update_last_loaded_date(tableName,connection):
    cursor = connection.cursor()
    try:
        current_time =datetime.now()
        query = f"INSERT INTO etl_metadata(table_name,last_loaded_date) VALUES ('{tableName}','{current_time}') ON DUPLICATE KEY UPDATE last_loaded_date='{current_time}'"
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        #print(f"Error updating last loaded date for {tableName}: {str(e)}")
        connection.rollback()
        
# Filter the data based on last loaded date for incremental load    
def filter_incremental_data(df,timestamp_column,last_loaded_timestamp):
    if last_loaded_timestamp is not None:
        #print(f"Filtering data for incremental load based on last loaded timestamp: {last_loaded_timestamp}")
        #print(f"DataFrame {timestamp_column} column sample:\n{df[timestamp_column].head()}")        
        filtered_df = df[df[timestamp_column] > last_loaded_timestamp]
        #print(f"Filtered DataFrame size: {len(filtered_df)}")
        return filtered_df
    else:
        return df

