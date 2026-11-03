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


# 4. Define Mapping : Business Key -> List of possible label
METRIC_MAP = {
        'total_revenue': ['Total Operating Revenue', 'Revenue', 'Net Sales'],
        'total_opt_cost': ['Total Operating Costs', 'Operating Cost'],
        'gross_profit':   ['Gross Profit', 'Total Gross Profit'],
        'total_opt_exp':  ['Total Operating Expenses', 'Operating Expense'],
        'net_income' : ['Net Income', 'Pre-tax Profit (Loss)']
    }

# Sanitization layer - Making sure data is clean when imported.
# Make sure there are no empty spaces, $, in the numbers
# Convert () to -(negative)
def sanitize_financial_value(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    
    if col_name in df.columns:
        df[col_name] = (
            df[col_name]
            .astype(str)
            .str.replace(r'[$,]', '', regex=True) 
            .str.replace(r'\((.*?)\)', r'-\1', regex=True)
            .pipe(pd.to_numeric, errors='coerce')
        )
    return df
    

def load_income_statement(file_name) -> pd.DataFrame:
    
    target_path = DATA_FOLDER / file_name
    print(target_path)
    
    # 1. Check: Does the file actually exist?
    if not target_path.exists(): 
        raise FileNotFoundError(f"Critical Error: Could not find {file_name} at {target_path}")
    print(f"Found file :{target_path}")
    
    # 2. Load faile to DataFrame obj
    df = pd.read_excel(
        target_path,
        skiprows=1,        # Skip "Table 1"
        index_col=0        # Set "English Description" as the index
        )
    
    # 3. sanitization to entire column
    sanitize_financial_value(df, "Actual Amount")
    sanitize_financial_value(df, "Budgeted Amount")
    
    return df

# Find value through loop (Slow)
def find_value(df, key) -> float:
    for name in METRIC_MAP[key]:
        if name in df.index:
            return float(df.loc[name, "Actual Amount"])
    
    print(f"Table does not contain the name in {key}")
    return 0.0

# Find value through Pandas' Set Logic
def find_value_index(df: pd.DataFrame, key: str) -> float:
    aliases = METRIC_MAP.get(key,[])
    #print(f"LOG: Print what aliases contain{aliases}")
    common = df.index.intersection(aliases)
    #print(f"LOG: Print what is common: {common}")
    
    if not common.empty:
        return float(df.loc[common[0], "Actual Amount"])
    
    print(f"Table does not contain the name in {key}")
    return 0.0


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

def extract_financial_metic(df):
        
    metrics = {}
    
    # 1. Converty the entire column to numeric
    #df["Actual Amount"] = pd.to_numeric(df["Actual Amount"], errors='coerce')
    
    
    # 2. Extract & simple math
    metrics['total_revenue'] = find_value_index(df, 'total_revenue')
    metrics['total_opt_cost'] = find_value_index(df, 'total_opt_cost')
    metrics['gross_porofit'] = find_value_index(df, 'gross_profit')
    metrics['total_opt_expense'] = find_value_index(df, 'total_opt_exp')
    metrics['opt_income'] = metrics['gross_porofit'] - metrics['total_opt_expense']
    metrics['net_income'] = find_value_index(df, 'net_income')
    metrics['net_profit_margin'] = metrics['net_income'] / metrics['total_revenue']
    
    # metrics = {k: float(v) for k, v in metrics.items()}
    
    print(f"Extract_metric: {metrics}")


# --- Execution ----
try:
    df = load_income_statement("2024q1_income.xlsx")
        # Basic validation before accessing numbers
        # print(df.head(10))      # Check: Does the top look like a clean table
        # print(df.tail(10))
        #print(df.dtypes)        # Check: Actual Ammount now a number/float instead of an object
        #print(df.isna().sum())  # Are there any Nans    
except Exception as e:
    print(e)
    
extract_financial_metic(df)

