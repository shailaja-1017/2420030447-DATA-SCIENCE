

import seaborn as sns
tips = sns.load_dataset("tips")
print(tips.head())

iris = sns.load_dataset("iris")
print(iris.head())

titanic = sns.load_dataset("titanic")
print(titanic.head())

#Define the problem
objective = "Classification: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalanced classes"
print("Objective:",objective)
print("Success Criteria:",success_criteria)
print("Constraints:",constraints)

#Data collection
df = sns.load_dataset("titanic")
print("Data shape:",df.shape)
print(df.head())

print(df.info())

print(df.describe())

#Data cleaning & preprocessing
import seaborn as sns
import pandas as pd
df = sns.load_dataset("titanic")
df['age'].fillna(df['age'].median(),inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0],inplace=True)
df.drop_duplicates(inplace=True)
df = pd.get_dummies(df,columns=['sex','class','embarked'],drop_first=True)
df['family_size'] = df['sibsp']+df['parch']
print(df.head())

df = pd.read_csv('student.csv')
df

#Exploratory Data Analysis(EDA)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = sns.load_dataset("titanic")
sns.histplot(df['age'],bins=20,kde=True)
plt.title("Age distribution")
plt.show()

df = sns.load_dataset("tips")
sns.histplot(df['size'],bins=10,kde=True)
plt.title("size")
plt.show()

df = pd.read_csv('student.csv')
data = df["attendance"]
plt.hist(data,bins=10)
plt.title("attendance")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("tips")
corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation matrix")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student.csv")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()
