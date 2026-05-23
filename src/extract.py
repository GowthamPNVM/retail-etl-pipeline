import pandas as pd
from validation import validate_file_exists,validate_column

def extract_csv(filePath,expectedColumns):
    validate_file_exists(filePath)
    df = pd.read_csv(filePath)
    validate_column(df,expectedColumns)

    return df
