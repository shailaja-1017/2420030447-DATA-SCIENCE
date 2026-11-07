

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
plt.figure(figsize=(6,4))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title("Histogram of Sepal Length")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['sepal length (cm)'])
plt.title("Boxplot of Sepal Length")
plt.show()

species_counts = df['species'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(species_counts, labels=iris.target_names, autopct='%1.1f%%', startangle=90)
plt.title("Species Distribution")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=tips['total_bill'])
plt.title("Boxplot of Total Bill")
plt.show()

species_counts = tips['smoker'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Smoker Distribution")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({i:name for i, name in enumerate(iris.target_names)})

plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sepal length (cm)'], y=df['sepal width (cm)'],
                hue=df['species_name'], palette='Set1')
plt.title("Scatter Plot of Sepal Length vs Sepal Width")
plt.show()

plt.figure(figsize=(6,4))
plt.plot(df['sepal length (cm)'])
plt.title("Line Plot of Sepal Length")
plt.xlabel("Simple Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=df['species_name'], y=df['sepal length (cm)'])
plt.title("Bar Plot of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.scatterplot(x=tips['total_bill'], y=tips['tip'],
                hue=tips['sex'], palette='Set1')
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

plt.figure(figsize=(6,4))
plt.plot(tips['total_bill'])
plt.title("Line Plot of Total Bill")
plt.xlabel("Simple Index")
plt.ylabel("Total Bill")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=tips['day'], y=tips['total_bill'])
plt.title("Bar Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

#Multivariate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({i:name for i, name in enumerate(iris.target_names)})

plt.figure(figsize=(6,4))
sns.heatmap(df.iloc[:, :-1].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Iris Features")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], s = df['petal length (cm)'] * 20, alpha=0.5, c=df['species'], cmap='viridis')
plt.title("Bubble Plot of Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()

sns.pairplot(df.iloc[:, :4])
plt.suptitle("Pair Plot of Iris Features, y = 1.02")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

df = pd.DataFrame(tips)

plt.figure(figsize=(6,4))

sns.heatmap(df.select (http://df.select/)_dtypes(include='number').corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap of Tips Features")

plt.show (http://plt.show/)()

plt.figure(figsize=(6,4))

plt.scatter(df['total_bill'], df['tip'], s=df['size'] * 20, alpha=0.5, c=df['size'], cmap='viridis')

plt.title("Bubble Plot of Total Bill vs Tip")

plt.xlabel("Total Bill")

plt.ylabel("Tip")

plt.show (http://plt.show/)()

sns.pairplot(df.select (http://df.select/)_dtypes(include='number'))

plt.suptitle("Pair Plot of Tips Features", y=1.02)

plt.show (http://plt.show/)()

#Advanced techniques
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
plt.figure(figsize=(6,4))
sns.violinplot(x=df['species'], y=df['sepal length (cm)'])
plt.title("Violin Plot of Sepal Length by Species")
plt.xticks(ticks=[0, 1, 2], labels=iris.target_names)
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.violinplot(x=tips['day'], y=tips['total_bill'])
plt.title("Violin Plot of Total Bill by Day")
plt.show()