import pandas as pd
import numpy as np

"""
# Name: test_sanitize_scale_handler.py
Test sanitize_financial_numbers() function:
- Make sure this piece of code works.  Because current data show Panda automatically sanitized the data
- Still need to add this just in case future data does not convert nicely

# NEXT:::
 -> Implement "Scale" Handler - k -> 1,000 M -> 1,000,000
- test_data: $1.2M -> 1,200,000
"""


test_data = {
    "Actual Amount": ["$1,200.50", "(500.00)", "10,000", "N/A", "", np.nan, "$1.2M"],
    "Budgeted Amount": ["$2,000", "100", "(1,000.00)", "TBD", "0", np.nan, "Unknown"]
}


# Clean only 
# $(dollar sign), 
# ',' (comma between numbers ex: 1,000)
# ' ' emply space
def clean_num_column(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    if col_name in df.columns:
        df[col_name] = (
            df[col_name]
            .astype(str)                                   # Convert to string
            .str.replace(r'[$,]', '', regex=True)          # Find $ sign or , comma replace with nothing
            .str.replace(r'\((.*?)\)', r'-\1', regex=True) # Handles (100) -> -100 across whole column
            .pipe(pd.to_numeric, errors='coerce')          # .pipe() pass clean string directly into `pd.to_numeric` converts entire column to float64.
        )
    return df
    

# Sanitize data
def sanitize_financial_numbers(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    
    df_test = pd.DataFrame(test_data)
    
    # Orchestration Layer - 2 methods with different level of sanitization....
    # Standard sanitization
    # clean_num_column(df_test, "Actual Amount")
    
    # Magnitude Handler {'K': 1e3, 'M': 1e6, 'B': 1e9}
    
    print(f"Original df: {df_test}") 
    
    return None


# 2. Run the cleaning function
df_cleaned = sanitize_financial_numbers(df_test.copy(), "Actual Amount")
df_cleaned = sanitize_financial_numbers(df_cleaned, "Budgeted Amount")

print(df_cleaned)