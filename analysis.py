
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


# correlation by selecting data types

x = df.select_dtypes(include=[float, int])
correlation = x.corr()
print(correlation)


#correlation between specific two columns
col1 = df['Sales']
col2 = df['Postal Code']

print(df[['Sales', 'Postal Code']].corr().iloc[0, 1])


correlation = col1.corr(col2)







