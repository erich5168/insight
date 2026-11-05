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


df = pd.DataFrame(test_data)

df_copy = df.copy()    
  
print(f"Original df: {df_copy}") 

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

def parse_magnitude(val):    
    
    # 1. If field is empty return with np.nan.  We do this 1st so we don't wast compute power.
    if pd.isna(val) or val == "" : return np.nan
    
    # 2. Clean and strip cell replace $ with ''(empty string)
    # [float] -> [str]
    clean_str =  str(val).replace('$', '').replace(',', '').strip().upper()
    
    # 3. Handle accounting negative (parentheses) and standard numbers   
    if clean_str.startswith("(") and clean_str.endswith(")"):
        clean_str = "-" + clean_str.replace("(", "").replace(")", "")

    # 4. Check if the last character is a known multiplier
    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}

    print(f"Print the last character{clean_str[-1]}")
    if clean_str[-1] in multipliers:
        unit = clean_str[-1]
        number_part = pd.to_numeric(clean_str[:-1], errors='coerce')    # Everything except the last character [  ]
        
        clean_str = number_part * multipliers[unit]

    return clean_str


def parse_magnitude_ai(val):
    if pd.isna(val) or val == "": return np.nan
    
    # Clean basic symbols first
    clean_str = str(val).replace('$', '').replace(',', '').strip().upper()
    
    # Magnitude Map
    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}
    
    # Check if the last character is a known multiplier
    if clean_str[-1] in multipliers:
        unit = clean_str[-1]
        number_part = clean_str[:-1] # Everything except the last char
        try:
            return float(number_part) * multipliers[unit]
        except ValueError:
            return np.nan
            
    # Handle accounting negatives (parentheses) and standard numbers
    if clean_str.startswith('(') and clean_str.endswith(')'):
        clean_str = '-' + clean_str[1:-1]
    
    return pd.to_numeric(clean_str, errors='coerce')
    
    
# Sanitize data
def sanitize_financial_numbers(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    # Orchestration Layer - 2 methods with different level of sanitization....
    
    # Magnitude Handler {'K': 1e3, 'M': 1e6, 'B': 1e9}
    
    # Connect to parse_magnitude : it only takes one value
    df_copy[col_name] = df_copy[col_name].apply(parse_magnitude)
    
    # Standard sanitization
    # return clean_num_column(df_copy, "Actual Amount")


# 2. Run the cleaning function
# df_cleaned = sanitize_financial_numbers(df_copy, "Actual Amount")
# df_cleaned = sanitize_financial_numbers(df_cleaned, "Budgeted Amount")

# print(df_cleaned)

sanitize_financial_numbers(df_copy, "Actual Amount")

print(f"After cleaning {df_copy}")
print('--------')
print(f"Data type {df_copy.dtypes}")
actual_col_val = df_copy.loc[6, "Actual Amount"]
print(f"ROW 2, Actual Amount: {actual_col_val}")
print(type(actual_col_val))
print('--------')
print(f"Data type {df_copy.isna().sum()}")