import pandas as pd
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)
print(df.groupby('Department')['Salary'].mean())

print(df.groupby('Department')['Salary'].max())

#print(df[(df['Age'] > 30) & (df['City'] == 'New York')])
print(df[(df['Experience'] > 5 & (df['Salary'] > 65000))])