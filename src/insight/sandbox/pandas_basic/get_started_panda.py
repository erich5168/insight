import pandas as pd

# 1. Create a dictionary with some data
data = {
    'Fruit': ['Apple', 'Banana', 'Cherry'],
    'Quantity': [10, 5, 8],
    'Price': [0.50, 0.30, 1.20]
}

# 2. Convert that dictionary into a DataFrame
df = pd.DataFrame(data)
print(df)

print('---------')

# A. Create Data Frame called emplyee
# B. 2 Column with 3 Name
# C. 3 Departments

raw_data = {
    'Name': ['Jake', 'Frances', 'Max'],
    'Department': [ 'Sales', 'Marketing', 'R&D' ]
}

employee = pd.DataFrame(raw_data)
print(employee)
print('---------')

print('Names Only variable')
names_only = employee['Name']
print(names_only)

print('---------')

print('Department series')
dept_series = employee['Department']
print('----')
print(dept_series)
print('----')
print(employee.tail(1))
print('----')
print(employee.info())

print('----')
print('Where Clause')
# "Give me the rows in employee where the Department is equal to Sales"
sales_staff = employee[ employee['Department'] == 'Sales' ]

print(sales_staff)
