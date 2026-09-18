import pandas as pd
import seaborn as sns
df = sns.load_dataset("tips")
print("First 5 rows of the dataset:")
print(df.head())
skewness_values = df.skew(numeric_only=True)
print("\nSkewness values:")
print(skewness_values)
kurtosis_values = df.kurtosis(numeric_only=True)
print("\nKurtosis values:")
print(kurtosis_values)
