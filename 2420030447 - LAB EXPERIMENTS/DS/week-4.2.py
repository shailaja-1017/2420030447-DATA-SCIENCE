import seaborn as sns
import pandas as pd
df=sns.load_dataset("titanic")
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df.drop_duplicates(inplace=True)
df=pd.get_dummies(df, columns=['sex','class','embarked'], drop_first=True)
df['family_size'] = df['sibsp'] + df['parch']
print(df.head())