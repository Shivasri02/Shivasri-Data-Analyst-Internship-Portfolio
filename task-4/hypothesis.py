import pandas as pd
from scipy.stats import ttest_ind

# Load dataset (fix encoding issue)
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Check available categories (optional but useful)
print("Available Categories:", df['Category'].unique())

# Select two categories for comparison
category1 = df[df['Category'] == 'Technology']['Sales']
category2 = df[df['Category'] == 'Furniture']['Sales']

# Perform T-test
t_stat, p_value = ttest_ind(category1, category2, equal_var=False)

# Print results
print("\nT-statistic:", t_stat)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Result: Significant difference (Reject Null Hypothesis)")
else:
    print("Result: No significant difference (Fail to Reject Null Hypothesis)")

#Hypothesis testing