import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PCA
tips=sns.load_dataset("tips")
numeric_cols=tips.select_dtypes(include=['float64','int64']).columns
scaler=StandardScaler()
scaled_data=scaler.fit_transform(tips[numeric_cols])
pca=PCA(n_components=2)
pca_result=pca.fit_transform(scaled_data)
pca_df=pd.DataFrame(data=pca_result, columns=['PC1','PC2'])
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("\nPCA Result:")
print(pca_df.head())