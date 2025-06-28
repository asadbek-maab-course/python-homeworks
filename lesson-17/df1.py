import pandas as pd
from IPython.core.display_functions import display

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000],
    'Bonus': [5000, 6000, 7000, 8000, 9000, 10000]
}

def fn(a):
    return 2*a

df = pd.DataFrame(data)
df['Salary'].apply(fn)

def salary_bonus(row):
    return int(row['Salary']) + int(row['Bonus'])
df['total_money'] = df.apply(salary_bonus, axis=1)
print(df.columns)
sorted_df = df.sort_values(by='total_money', axis=0, ascending=False)
print(sorted_df)