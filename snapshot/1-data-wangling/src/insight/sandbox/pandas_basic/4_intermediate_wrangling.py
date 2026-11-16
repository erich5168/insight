import pandas as pd

## Groupby
def groupby_ex():
    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
        'Dept': ['Sales', 'Sales', 'IT', 'IT'],
        'Salary': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # "Group by Dept, look at the Salary column, and find the mean (average)"
    avg_salary = df.groupby('Dept')['Salary'].mean().reset_index()

    print(avg_salary)

# groupby_ex()

def groupby_checkpoint():
    
    data = {
        'Store': ['North', 'North', 'South', 'South', 'East', 'East'],
        'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Banana'],
        'Sales': [100, 150, 200, 50, 300, 100]
    }
    df_sales = pd.DataFrame(data)
    print(df_sales)
    
    # Challenge
    # 1. The regional manager wants to know the Total Sales (the sum) for each Store.
    store_totals = df_sales.groupby('Store')['Sales'].sum().reset_index()
    print(store_totals)

# groupby_checkpoint()    

## Aggregation - pass a list of multiple calculation

def aggregate_method ():

    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Department': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR'],
        'Salary': [50000, 60000, 70000, 80000, 45000, 55000],
        'Experience_Years': [2, 5, 3, 10, 1, 6]
    }
    df_company = pd.DataFrame(data)
    
    dept_salary_summary = df_company.groupby('Department')['Salary'].agg(['mean', 'max']).reset_index()
    print(dept_salary_summary)

# aggregate_method()


# C. Adding new Columns (Vectorized Operations)

def vectorized_opt ():

    data = {
        'Product': ['Laptop', 'Mouse', 'Monitor'],
        'Price': [1200, 25, 300],
        'Quantity_Sold': [5, 100, 20]
    }
    df_sales = pd.DataFrame(data)
    
    # Main: The finance team needs to know the total revenue for each product
    # 1. Create new column called "Revenue" (which is Price x Quantity_Sold)
    df_sales['Revenue'] = df_sales['Price'] * df_sales['Quantity_Sold']
    # 2. Create another column called "Tax" (15% of the Revenue.)
    df_sales['Tax'] = df_sales['Revenue'] * 0.15
    
    df_sales['Revenue_After_Tax'] = df_sales['Revenue'] - df_sales['Tax']
    
    print(df_sales)
    
# vectorized_opt()
    
# D. Merging Datasets

def table_merge():

    # Table A: Employees and their Dept ID
    df_emp = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'DeptID': [10, 20, 10]
    })

    # Table B: Dept ID and the actual Dept Name
    df_dept = pd.DataFrame({
        'DeptID': [10, 20],
        'DeptName': ['Engineering', 'Marketing']
    })
    
    # Challenge:
    # From `DeptID` (numbers), but want to see actual `DeptName`.
    # Instructions:
    # Merge df_emp and df_dept using common `DeptID`.  Store the result in `df_employee_details.`
    
    df_employee_details = pd.merge(df_emp, df_dept, on = 'DeptID')
    
    print(df_employee_details)
    
    
table_merge()

