import pandas as pd
import sqlite3

# Task 1: Reading Files

conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("Customers table (first 10 rows):")
print(customers_df.head(10))

iris_df = pd.read_json('iris.json')
print("\nIris dataset shape:", iris_df.shape)
print("Columns:", iris_df.columns.tolist())

titanic_df = pd.read_excel('titanic.xlsx')
print("\nTitanic dataset (first 5 rows):")
print(titanic_df.head())

flights_df = pd.read_parquet('flights.parquet')
print("\nFlights DataFrame info:")
flights_df.info()

movie_df = pd.read_csv('movie.csv')
print("\nRandom sample of 10 movies:")
print(movie_df.sample(10))

# Task 2: Exploring DataFrames

iris_df.columns = iris_df.columns.str.lower()
sepal_df = iris_df[['sepal_length', 'sepal_width']]
print("\nSelected columns from iris:")
print(sepal_df.head())

age_above_30 = titanic_df[titanic_df['Age'] > 30]
print("\nPassengers with age > 30:")
print(age_above_30.head())

gender_counts = titanic_df['Sex'].value_counts()
print("\nGender value counts:")
print(gender_counts)

flight_cols = flights_df[['origin', 'dest', 'carrier']]
print("\nSelected columns from flights:")
print(flight_cols.head())

unique_dests = flights_df['dest'].nunique()
print("\nNumber of unique destinations:", unique_dests)

long_movies = movie_df[movie_df['duration'] > 120]
sorted_long_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nLong movies sorted by director Facebook likes:")
print(sorted_long_movies[['director_name', 'duration', 'director_facebook_likes']].head())

# Task 3: Challenges and Explorations

print("\nIris statistics:")
print(iris_df.describe().loc[['mean', '50%', 'std']])

print("\nTitanic age stats:")
print("Min age:", titanic_df['Age'].min())
print("Max age:", titanic_df['Age'].max())
print("Sum of ages:", titanic_df['Age'].sum())

top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
top_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum().max()
print("\nTop director by total Facebook likes:", top_director, "(", top_likes, ")")

top5_longest = movie_df.nlargest(5, 'duration')[['director_name', 'movie_title', 'duration']]
print("\nTop 5 longest movies:")
print(top5_longest)

print("\nMissing values in flights:")
print(flights_df.isnull().sum())

if 'dep_delay' in flights_df.columns:
    flights_df['dep_delay'].fillna(flights_df['dep_delay'].mean(), inplace=True)
    print("\nMissing values in 'dep_delay' filled with mean.")
