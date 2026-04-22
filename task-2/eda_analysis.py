import pandas as pd

df = pd.read_csv(r"C:\Users\bachu\OneDrive\Desktop\EDA_task2\Sample - Superstore.csv", encoding='latin1')

#load dataset
print(df.head())


#data undrestanding
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nInfo:")
print(df.info())
print("\nStatistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())


#data cleaning
#deletes missing values
# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed')

# Create Month column
df['Month'] = df['Order Date'].dt.to_period('M')

import matplotlib.pyplot as plt
import seaborn as sns

#graphs # using groupby
# 1. Category Sales
df.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Category")
plt.show()

# 2. Region Sales
df.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Region")
plt.show()

# 3. Sales vs Profit
plt.scatter(df['Sales'], df['Profit'])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()

# 4. Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()

# 5. Profit Distribution
df['Profit'].hist()
plt.title("Profit Distribution")
plt.show()


import pandas as pd
import sqlite3
# Load CSV
df = pd.read_csv(r"C:\Users\bachu\OneDrive\Desktop\EDA_task2\Sample - Superstore.csv", encoding='latin1')

# Create database
conn = sqlite3.connect("superstore.db")

# Convert CSV → SQL table
df.to_sql("superstore", conn, if_exists='replace', index=False)

print("Data imported successfully!")


