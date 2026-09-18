import seaborn as sns
import pandas as pd
df = pd.read_csv("student.csv")

df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df.drop_duplicates(inplace=True)
df = pd.get_dummies(df, columns=["sex", "class", "embarked"], drop_first=True)
df["family_size"] = df["sibsp"] + df["parch"]

print(df.head())