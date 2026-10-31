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


# --- Execution ----
try:
    df = load_income_statement("2024q1_income.xlsx")
    print(df.head(10))
    print(df.dtypes)
    print(df.isna().sum())
except Exception as e:
    print(e)