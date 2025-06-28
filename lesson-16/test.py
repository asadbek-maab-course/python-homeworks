import pandas as pd

PATH = "/media/asadbek/D/maab/new/python-homeworks/lesson-16/"

# df = pd.read_csv(PATH + "data/employee.csv")
df_iris = pd.read_json(PATH + 'data/iris.json')
df_iris['id'] = [i for i in range(1, len(df_iris) + 1)]
a = df_iris.sort_values(by = ['sepalLength'])
b = df_iris.select_dtypes('number')
print(b)
