import pandas as pd
import numpy as np

# Phase 3: Data cleaning
def data_cleaning():
    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
        'Sales': [200, np.nan, 150, np.nan],
        'Bonus': [50, 20, np.nan, 10]
    }
    df_staff = pd.DataFrame(data)

    print(df_staff)
    print('------')

    df_final = df_staff.fillna(0)

    print(df_final)
    print('------------')


#data_cleaning()

# Phase 3 Data Types and Renaming

def data_type_renaming ():
        
    data2 = {
        'emp_id': [101, 102, 103],
        'salary_usd': [50000.0, 60000.0, np.nan],
        'dept_code': ['A', 'B', 'A']
    }
    df_hr = pd.DataFrame(data2)

    print(df_hr)

    print('-------')

    # Challenge:
    # 1. File the missing 'salary_usd' with 0
    df_hr = df_hr.fillna(0)
    # 2. Convert the 'salary_usd' column to an integer
    df_hr['salary_usd'] = df_hr['salary_usd'].astype(int)
    
    print('Experiement = salary_usd')
    print(df_hr['salary_usd'].astype(int))
    
    # 3. Renaming the 'dept_code' column to "Department"
    df_hr = df_hr.rename(columns={'dept_code': 'Department'})
    #.rename(columns={'dept_code': 'Department'})

    print(df_hr)
    print('------------')

data_type_renaming()


def data_type_renaming_refine ():
    
    data2 = {
        'emp_id': [101, 102, 103],
        'salary_usd': [50000.0, 60000.0, np.nan],
        'dept_code': ['A', 'B', 'A']
    }
    df_hr = pd.DataFrame(data2)

    print(df_hr)

    print('-------')
    
    # This is how the pros do it!
    df_final = (df_hr
        .fillna(0)
        .astype({'salary_usd': int})
        .rename(columns={'dept_code': 'Department'}))

    print(df_final)
    print('------------')
    
# data_type_renaming_refine()


# Phase 3 Basic String

def data_cleaning_str ():
    data = {
        'Product_Code': ['  prod_101  ', 'PROD_102', ' prod_103'],
        'Category': [' electronics ', 'ELECTRONICS', 'Electronics']
    }
    df_inventory = pd.DataFrame(data)
    
    print(df_inventory)
    
    print('----------------')
    
    # 1. Clean Product_Code: Remove the extra spaces and make everything uppercase.
    # 2. Clean Category: Make everything lowercase so they all match perfectly.
    
    df_inventory['Product_Code'] = df_inventory['Product_Code'].str.strip().str.upper()
    df_inventory['Category'] = df_inventory['Category'].str.lower()
    
    print(df_inventory)


#data_cleaning_str()