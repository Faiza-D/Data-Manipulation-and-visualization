
import pandas as pd

df = pd.read_csv('C:/PythonProject/sales.csv')

print(df.info())
print(df.describe())
print(df.head())
print(df.tail())

# Data CLEANING

print(pd.isnull(df).sum())
df.dropna(inplace= True)
print(df.info())
print(df.duplicated())
df.drop_duplicates(inplace= True)
print(df.info())






