import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("student.csv")
corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()