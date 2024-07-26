import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/PythonProject/sales.csv')

# line plot
plt.figure(figsize=(15, 10))
print(sns.lineplot(x='State', y='Sales', data=df))
plt.title('Line Plot')
plt.xlabel('State')
plt.ylabel('Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()

# scatter plot
plt.figure(figsize=(15, 10))
print(sns.scatterplot(x='State', y='Sales', data=df))
plt.title('scatter Plot')
plt.xlabel('State')
plt.ylabel('Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


#bar plot
plt.figure(figsize=(15, 10))
print(sns.barplot(x='State', y='Sales', data=df))
plt.title('Bar Plot')
plt.xlabel('State')
plt.ylabel('Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# shows total sales by sub category using matplotlib
plt.figure(figsize=(15, 10))
plt.bar(df['Sub-Category'], df['Sales'], color='red')
plt.title('Total Sales by Sub-Category')
plt.xlabel('Sub-Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()

# shows total sales by states using matplotlib
plt.figure(figsize=(15, 10))
plt.bar(df['State'], df['Sales'], color='skyblue')
plt.title('Total Sales by State')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# shows total sales by region using matplotlib
plt.figure(figsize=(15, 10))
plt.bar(df['Region'], df['Sales'], color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()