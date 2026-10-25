import pandas as pd

def view_copy ():

    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Dept': ['Sales', 'IT', 'Sales', 'IT'],
        'Salary': [50000, 60000, 55000, 65000]
    }
    df_company = pd.DataFrame(data)
    
    print(df_company)
    
    print('df_company ____ original')
    """
    Your challenge:
    The company wants to give a $5,000 bonus ONLY to the employees in the 'Sales' department.

    Instead of creating a new DataFrame, write one line of code using .loc to increase the Salary of all 'Sales' employees by 5,000 directly in the df_company DataFrame.

    (Hint: df.loc[condition, 'column_name'] = new_value)
    """
    
    df_company.loc[ df_company['Dept'] == 'Sales', 'Salary' ] += 5000

    print(df_company)
    
view_copy()