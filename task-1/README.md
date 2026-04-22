# 📊 Data Wrangling Project

## 📌 Project Overview
This project focuses on applying data wrangling techniques to a customer purchase dataset. The goal is to assess data quality, clean inconsistencies, and prepare the dataset for further analysis.

## 📂 Dataset
The dataset contains customer purchase information with the following features:
- Customer_ID  
- Name  
- Age  
- Gender  
- City  
- Purchase_Amount  
- Purchase_Date  
- Product_Category  

## 📖 Data Understanding
- Initial dataset contained multiple records with mixed data types
- Both numerical and categorical data were present
- Dataset required cleaning for accurate analysis

## 🔍 Data Quality Assessment
The dataset was evaluated for:
- Missing values  
- Duplicate records  
- Data type inconsistencies  
- Outliers  

### Observations:
- Missing values found in:
  - Customer_ID (32 records)
  - Total_Amount (34 records)
- No missing values in other columns
- No major duplicate issues identified

## 🧹 Data Cleaning Steps
- Removed duplicate records  
- Handled missing values  
- Converted `Purchase_Date` to datetime format  
- Created a new feature: **Age_Group**  

## 🛠 Tools & Technologies
- Python  
- Pandas  
- Excel  
- VS Code  

## 📤 Output
- Cleaned dataset saved as: `cleaned_dataset.csv`

## 📈 Key Learnings
- Data cleaning and preprocessing techniques  
- Handling missing and inconsistent data  
- Feature engineering basics  
- Importance of data quality in analysis  

## ✅ Conclusion
This project demonstrates the importance of data wrangling as a foundational step in the data analysis process. Clean and structured data ensures more accurate and reliable insights.
