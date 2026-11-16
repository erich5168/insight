# Data Wragling :: Notes

## load.py

### Responsibility
#### 1. Load excel to `DataFram` object
    - [ ] global sanitaization phase
        - Take care of $ & , signs

```python
def load_and_clean_financials(filepath):
    df = pd.read_csv(filepath) # or read_excel
    
    if "Actual Amount" in df.columns:
        # Apply sanitization to the entire series at once
        df["Actual Amount"] = (
            df["Actual Amount"]
            .astype(str)
            .str.replace(r'[$,]', '', regex=True) 
            .str.replace(r'\((.*?)\)', r'-\1', regex=True)
            .pipe(pd.to_numeric, errors='coerce')
        )
    return df

```

**Line-by-Line Mechanics:**
- astype(str): Ensures the entire column is treated as strings before we apply string methods, preventing crashes if some cells are already numbers.
- str.replace(r'[$,]', '', regex=True): This uses a Regular Expression. [$,] tells Pandas: "Find any character that is either a dollar sign or a comma and replace it with nothing." This is significantly faster than chaining .replace().replace().
- str.replace(r'\((.*?)\)', r'-\1', regex=True): This is a Regex "Capture Group." It looks for anything inside parentheses (...) and replaces it with a minus sign followed by the content of those parentheses. This handles accounting negatives (100) → -100 across the whole column in one pass.
- pipe(pd.to_numeric, errors='coerce'): The .pipe() method allows us to pass the cleaned string series directly into pd.to_numeric. This converts the entire column from object (strings) to float64 in one vectorized operation.

 - [ ] multiplier {'K': 1e3, 'M': 1e6, 'B': 1e9}

```python
def parse_magnitude(val):
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

# Usage in clean_financials:
def clean_financials(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    if col_name in df.columns:
        df_copy = df.copy()
        # Use .apply instead of the .str chain for complex logic
        df_copy[col_name] = df_copy[col_name].apply(parse_magnitude)
        return df_copy
    return df

```

#### 2. Matrice map - provide alternative naming for each column
#### 3. Extract Data
#### 4. Manipulate, KPI Calc




## test_code

Testing sanitization code.  Because by default `df.read_excel(...)` automatically sanitize numbers. This serves as a testing ground for the snippets.