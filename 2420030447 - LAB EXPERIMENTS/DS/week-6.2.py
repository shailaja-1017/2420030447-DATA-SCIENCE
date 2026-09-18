import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
print("first 5 rows of the dataset:")
print(df.head())
skewness_values = df.skew()
print("\nSkewness values:")
print(skewness_values)
kurtosis_values = df.kurtosis()
print("\nKurtosis values:")
print(kurtosis_values)