

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.DataFrame({
    'A': [10,20,30,40,50],
    'B' : [5,15,25,35,45]
})
print(data)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)
normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
print(normalized_df)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)
standardized_df = pd.DataFrame(standardized_data, columns=data.columns)
print(standardized_df)

df = pd.DataFrame({'Color':['Red','Blue','Green','Red','Blue']})
one_hot = pd.get_dummies(df,columns=['Color'])
print("\nOne-Hot Encoding")
print(one_hot)

import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
import seaborn as sns
tips = sns.load_dataset("tips")
print("Original Data (first 5 rows):")
print(tips.head())
numeric_cols = tips.select_dtypes(include=['float64', 'int64']).columns
scaler_minmax = MinMaxScaler()
tips_normalized = tips.copy()
tips_normalized[numeric_cols]= scaler_minmax.fit_transform(tips[numeric_cols])
print("\nNormalized Data (first 5 rows):")
print(tips_normalized.head())
#Standardization
scaler_standard = StandardScaler()
tips_standardized = tips.copy()
tips_standardized[numeric_cols]= scaler_standard.fit_transform(tips[numeric_cols])
print("\nStandardized Data (first 5 rows):")
print(tips_standardized.head())
#One-Hot Encoding
tips_onehot = pd.get_dummies(tips,columns=['sex','smoker','day','time'])
print("\nOne-Hot Encoded Data (first 5 rows)")
print(tips_onehot.head())

#PCA
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
tips = sns.load_dataset("tips")
numeric_cols = tips.select_dtypes(include=['float64', 'int64'])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_cols)
pca = PCA(n_components=2)
pca_results = pca.fit_transform(scaled_data)
pca_df = pd.DataFrame(data=pca_results,columns=['PC1','PC2'])
print("Explained Variance Ratio",pca.explained_variance_ratio_)
print("\nPCA Result")
print(pca_df.head())

import matplotlib.pyplot as plt
plt.scatter(pca_df['PC1'],pca_df['PC2'],alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection of Tips Dataset')
plt.show()
