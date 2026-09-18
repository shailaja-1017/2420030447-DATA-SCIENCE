import pandas as pd
import seaborn as sns
from statistics import mode
tips=sns.load_dataset("tips")
df=pd.DataFrame(data=tips.data, columns=tips.feature_names)
print("first 5 rows of the dataset:")
print(df.head())
mean_values = df.mean()
print("\nMean values:")
print(mean_values)
median_values = df.median()
print("\nMedian values:")
print(median_values)
mode_values = df.mode().iloc[0]
print("\nMode values:")
print(mode_values)
