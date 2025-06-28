## Merge and join
# -merge
import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)

merged = pd.merge(customers, invoices, on='CustomerId', how='inner')
invoice_counts = merged.groupby('CustomerId')['InvoiceId'].count().reset_index(name='TotalInvoices')

print(invoice_counts.head())

# -join
movies = pd.read_csv('movie.csv')

df1 = movies[['director_name', 'color']].drop_duplicates()
df2 = movies[['director_name', 'num_critic_for_reviews']].drop_duplicates()

left_join = pd.merge(df1, df2, on='director_name', how='left')
outer_join = pd.merge(df1, df2, on='director_name', how='outer')

print("Left join rows:", len(left_join))
print("Outer join rows:", len(outer_join))

## Grouping
# titanic
titanic = pd.read_excel('titanic.xlsx')

grouped = titanic.groupby('Pclass').agg(
    avg_age=('Age', 'mean'),
    total_fare=('Fare', 'sum'),
    passenger_count=('Pclass', 'count')
).reset_index()

print(grouped)

#multi level group
grouped_movies = movies.groupby(['color', 'director_name']).agg(
    total_reviews=('num_critic_for_reviews', 'sum'),
    avg_duration=('duration', 'mean')
).reset_index()

print(grouped_movies.head())

#nested
flights = pd.read_parquet('flights.parquet')

grouped_flights = flights.groupby(['Year', 'Month']).agg(
    total_flights=('FlightNum', 'count'),
    avg_arr_delay=('ArrDelay', 'mean'),
    max_dep_delay=('DepDelay', 'max')
).reset_index()

print(grouped_flights.head())

## Applying Functions
#1
def classify_age(age):
    if pd.isna(age):
        return 'Unknown'
    return 'Child' if age < 18 else 'Adult'

titanic['Age_Group'] = titanic['Age'].apply(classify_age)
print(titanic[['Age', 'Age_Group']].head())

#2
employees = pd.read_csv('employee.csv')

def normalize(group):
    group['Normalized_Salary'] = (group['Salary'] - group['Salary'].mean()) / group['Salary'].std()
    return group

normalized_employees = employees.groupby('Department').apply(normalize)
print(normalized_employees.head())

#3
def classify_duration(duration):
    if pd.isna(duration):
        return 'Unknown'
    elif duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movies['Length_Category'] = movies['duration'].apply(classify_duration)
print(movies[['duration', 'Length_Category']].head())


## pip
#1
def filter_survivors(df):
    return df[df['Survived'] == 1]

def fill_age(df):
    return df.assign(Age=df['Age'].fillna(df['Age'].mean()))

def add_fare_per_age(df):
    return df.assign(Fare_Per_Age=df['Fare'] / df['Age'])

pipeline_result = (
    titanic
    .pipe(filter_survivors)
    .pipe(fill_age)
    .pipe(add_fare_per_age)
)

print(pipeline_result[['Survived', 'Age', 'Fare_Per_Age']].head())

#2
def filter_delayed(df):
    return df[df['DepDelay'] > 30]

def add_delay_per_hour(df):
    return df.assign(Delay_Per_Hour=df['DepDelay'] / df['AirTime'])

pipeline_flights = (
    flights
    .pipe(filter_delayed)
    .pipe(add_delay_per_hour)
)

print(pipeline_flights[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())
