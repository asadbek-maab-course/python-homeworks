import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Add a new column 'C' which is the sum of 'A' and 'B'
df_new = df.assign(C=lambda x: x['A'] + x['B'])
print(df_new)

# Add multiple new columns
df_multiple = df.assign(
    D=[7, 8, 9],
    E=df['A'] * 2
)
print(df_multiple)