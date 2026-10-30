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

def load_income_statement(file_name):
    
    target_path = DATA_FOLDER / file_name
    print(target_path)
    
    # Check: Does the file actually exist?
    if not target_path.exists(): 
        raise FileNotFoundError(f"Critical Error: Could not find {file_name} at {target_path}")
    print(f"Found file :{target_path}")
    
    return pd.read_excel(target_path)
    


# --- Execution ----
try:
    df = load_income_statement("2024q1_income.xlsx")
    print(df.head())
except Exception as e:
    print(e)