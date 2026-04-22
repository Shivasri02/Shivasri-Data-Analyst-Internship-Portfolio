import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\bachu\OneDrive\Desktop\data_wrangling_t1\cleaned_sales_dataset.csv")

# Display first rows
print(df.head())

# Dataset info
print(df.info())

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Invoice_Date to datetime
df["Invoice_Date"] = pd.to_datetime(df["Invoice_Date"], format='mixed', dayfirst=True)

# Save cleaned dataset
df.to_csv("final_cleaned_dataset.csv", index=False)

print("Data cleaning completed successfully!")