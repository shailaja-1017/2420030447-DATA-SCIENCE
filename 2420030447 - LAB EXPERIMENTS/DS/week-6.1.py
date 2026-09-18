import pandas as pd
#import seaborn as sns
from sklearn.datasets import load_iris
#tips=sns.load_dataset("tips")
iris = load_iris()
df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
print("first 5 rows of the dataset:")
print(df.head())
range_values = df.max() - df.min()
print("\nRange values:")
print(range_values)
variance_values = df.var()
print("\nVariance values:") 
print(variance_values)
std_values = df.std()
print("\nStandard Deviation values:")
print(std_values)
q1=df.quantile(0.25)
q3=df.quantile(0.75)
IQR = q3 - q1
print("\nInterquartile Range (IQR) values:")
print(IQR)