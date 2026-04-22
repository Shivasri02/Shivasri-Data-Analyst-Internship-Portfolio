📊 Sales Data Analysis & Statistical Validation

Project Overview

This project focuses on analyzing sales data to uncover meaningful business insights and validate them using statistical methods.
The goal is to transform raw data into actionable insights that can support data-driven decision-making.



Objective

To analyze sales data, identify key trends and patterns, and validate findings using hypothesis testing to improve business performance.



 Dataset

The project uses the **Superstore Sales Dataset**, which contains transactional sales data.

 Key Features:

* Category (Furniture, Office Supplies, Technology)
* Sales
* Profit
* Order Date
* Quantity

This dataset helps in understanding product performance, customer behavior, and revenue trends.


 Data Analysis & Insights

 🔹 1. Product Performance

* Technology category generates the highest revenue.
* Indicates strong demand and profitability in this segment.

🔹 2. Sales Trend

* Sales show fluctuations over time with noticeable peak periods.
* Helps identify high-performing months.

 🔹 3. Sales vs Profit Relationship

* Positive relationship observed between sales and profit.
* Higher sales generally lead to higher profit, with some variations.



📈 Visualizations

The following visualizations were created:

* Bar Chart → Sales by Category
* Line Graph → Monthly Sales Trend
* Scatter Plot → Sales vs Profit

These visualizations help in better understanding patterns and trends in the data.


 Hypothesis Testing

 🔹 Hypothesis

* **H₀ (Null Hypothesis):** No significant difference in sales between categories
* **H₁ (Alternative Hypothesis):** Significant difference in sales between categories

 🔹 Method Used

A **T-test** was performed using Python (Pandas and SciPy) to compare sales between Technology and Furniture categories.

 🔹 Result

* **T-statistic:** 3.67
* **P-value:** 0.00024

 🔹 Conclusion

Since the p-value is less than 0.05, the result is statistically significant.
We reject the null hypothesis and conclude that sales differ significantly between categories.


 Business Impact

* Helps identify high-performing product categories
* Supports data-driven decision-making
* Enables better pricing and marketing strategies
* Improves overall sales performance


 Tools & Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* SciPy


 Conclusion

This project demonstrates how data analysis combined with statistical validation can provide meaningful insights.
It highlights the importance of using data-driven approaches for business growth and strategic planning.
