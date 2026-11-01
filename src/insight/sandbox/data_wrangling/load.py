import pandas as pd
from pathlib import Path
from insight.utils.paths import get_project_root

# EXECUTE: uv run python src/insight/sandbox/data_wrangling/load.py    

# 1. Get the absolute path of the current file
current_file = Path(__file__).resolve()

# 2. Get to the Project Root
PROJECT_ROOT = get_project_root()


# 3. Construct path of your data folder
DATA_FOLDER = PROJECT_ROOT / "data" / "processed"
FILE_BAL = DATA_FOLDER / "2024Q1_balance.xlsx"
FILE_INC = DATA_FOLDER / "2024q1_income.xlsx"

def load_income_statement(file_name) -> pd.DataFrame:
    
    target_path = DATA_FOLDER / file_name
    print(target_path)
    
    # Check: Does the file actually exist?
    if not target_path.exists(): 
        raise FileNotFoundError(f"Critical Error: Could not find {file_name} at {target_path}")
    print(f"Found file :{target_path}")
    
    df = pd.read_excel(
        target_path,
        skiprows=1,        # Skip "Table 1"
        index_col=0        # Set "English Description" as the index
        )
    
    return df



# 1. Leverage & Solvency
# Debtg-to-Equity Ratio
# Debt Ratio = Liabilities / Asset

# Equity Growthf


# 2. Liquidity
# Current Ratio = Asets / Liabilities
# Quick Ratio = (Assets - Inventory) / Liabilities

# Cash Buffer (in months) =
# Cash + Cash Equivalents / Average Monthly Operating Expenses

# Cash Buffer (in months) =
# Cash + Cash Equivalents / 
# ( Quarter Operating Expenses / 3)

def extract_metic():
    try:
        df = load_income_statement("2024q1_income.xlsx")
        
    except Exception as e:
        print(e)
        
    metrics = {}
    
    # 1. Converty the entire column to numeric
    #df["Actual Amount"] = pd.to_numeric(df["Actual Amount"], errors='coerce')
    
    
    # 2. Extract & simple math
    total_revenue = df.loc["Total Operating Revenue", "Actual Amount"]
    total_opt_cost = df.loc["Total Operating Costs" , "Actual Amount"]
    # For somereason "Gross Profit" number is returning datatype `timnedelta64` suggest cell is formatted as "Time Duration"
    # Use float() to convert the datatype
    gross_profit = float(df.loc["Gross Profit", "Actual Amount"])      
    total_opt_expense = df.loc["Total Operating Expenses", "Actual Amount"]
    
    metrics = {k: float(v) for k, v in metrics.items()}
    
    opt_income = gross_profit - total_opt_expense
    
    metrics['total_revenue'] = total_revenue
    metrics['total_opt_cost'] = total_opt_cost
    metrics['gross_porofit'] = gross_profit
    metrics['total_opt_expense'] = total_opt_expense
    metrics['opt_income'] = opt_income
    
    
    print(f"Extract_metric: {metrics}")


# --- Execution ----
try:
    # df = load_income_statement("2024q1_income.xlsx")
        # Basic validation before accessing numbers
        #print(df.head(10))      # Check: Does the top look like a clean table
        #print(df.dtypes)        # Check: Actual Ammount now a number/float instead of an object
        #print(df.isna().sum())  # Are there any Nans
    
    # total_revenue = df.loc["Total Operating Revenue", "Actual Amount"]
        #total_revenue = df.loc["Actual Amount", "Total Operating Revenue"]
    # print(f"Printing total_revenue - {total_revenue}")
    
    extract_metic()
    
except Exception as e:
    print(e)
    

