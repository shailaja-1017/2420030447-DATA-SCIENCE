import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 
df=sns.load_dataset("titanic")
sns.histplot(df['age'],bins=20, kde=True)
plt.title("Age Distribution")
plt.show()
df=sns.load_dataset("tips")
sns.histplot(df['size'],bins=10, kde=True)
plt.title("Family Size Distribution")
plt.show()
df=pd.read_csv("student.csv")
sns.histplot(df['attendence'],bins=10, kde=True)
plt.title("Attendence Distribution")
plt.show()
