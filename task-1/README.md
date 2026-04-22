Data Wrangling Internship Task
Project Overview
This project demonstrates data wrangling techniques on a customer purchase dataset.
The objective is to understand the dataset, assess its quality, clean the data, and prepare it for analysis.
Dataset
The dataset contains information about customer purchases including:
Customer_ID  
Name  
Age  
Gender  
City  
Purchase_Amount  
Purchase_Date  
Product_Category
The dataset contains 100 rows and 8 columns.
Data Dictionary
A data dictionary was created to explain the meaning and data type of each column.
Data Quality Assessment
The dataset was checked for the following:
Missing values
Duplicate records
Data type consistency
Outliers
No major issues were found.
Data Cleaning
Data cleaning was performed using Python and the Pandas library.
Steps performed:
Checked for missing values
Removed duplicate rows
Converted Purchase_Date to datetime format
Created an additional column called Age_Group
Tools Used
Python  
Pandas  
Excel  
VS Code
Output
The cleaned dataset was saved as cleaned_dataset.csv.
Data Quality Observations
The dataset consists of 300 records and 18 columns representing sales transactions.

Data Types
From df.info():

The dataset contains both numerical and categorical data types including integers, floats, and string values.

Missing Values:
Missing values were identified in the Customer_ID column (32 records) and Total_Amount column (34 records).

No Missing Values in Other Columns
All other columns contain complete data.
Invoice_ID → 0
Invoice_Date → 0
Product_ID → 0
Payment_Mode → 0
Country → 0

All other columns such as Invoice_ID, Product_ID, Payment_Mode, and Country did not contain missing values.

Data Cleaning Result
Data cleaning was performed using Python and the Pandas library. The dataset was inspected for missing values, duplicates, and data type consistency before saving the cleaned dataset.
