

!pip install numpy

!pip install pandas

import pandas as pd
import numpy as np
df = pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department':['HR','Finance', 'Finance',np.nan,'IT']})
print(df)
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)

#using forward fill
import pandas as pd
import numpy as np
df = pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department':['HR','Finance', 'Finance',np.nan,'IT']})
print("Original dataset with missing values:")
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)

#using backward fill
import pandas as pd
import numpy as np
df = pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department':['HR','Finance', 'Finance',np.nan,'IT']})
print("Original dataset with missing values:")
print(df)
df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)

#Drop rows with missing values
import pandas as pd
import numpy as np
df = pd.DataFrame({'Age':[25,30,np.nan,40,35], 'Department':['HR','Finance', 'Finance',np.nan,'IT']})
print("Original dataset :")
print(df)
df_drop_rows = df.dropna()
print("After dropping rows:\n",df_drop_rows)

#Deletion of cols with missing values using axis
df_drop_cols = df.dropna(axis=1)
print("After dropping columns:\n",df_drop_cols)

#Deletion of rows with missing values using axis
df_drop_rows = df.dropna(axis=0)
print("After dropping rows:\n",df_drop_rows)

#Removing Duplicates
import pandas as pd
df = pd.DataFrame({
    'ID':[1,2,2,3,4,4],
    'Name':['Alice','Bob','Bob','Charlie','David','David'],
    'Age':[25,30,30,35,40,40]
})
print("Original dataset:\n",df)
#Remove exact duplicates
df_exact = df.drop_duplicates()
print("\nAfter exact match removal:\n",df_exact)

#Subset based removal
import pandas as pd
df = pd.DataFrame({
    'ID':[1,2,2,3,4,4,5],
    'Name':['Alice','Bob','Bob','Charlie','David','David','David'],
    'Age':[25,30,30,35,40,40,40]
})
print("Original dataset:\n",df)
#Remove duplicates based on 'ID'
df_subset_id = df.drop_duplicates(subset=['ID'])
print("\nAfter subset-based removal (ID):\n",df_subset_id)
#Remove duplicates based on 'Name'
df_subset_name = df.drop_duplicates(subset=['Name'])
print("\nAfter subset-based removal (Name):\n",df_subset_name)

#Correcting Inconsistent Formats
import pandas as pd
df = pd.DataFrame({
    'Date': ['2025-01-05','05/01/2025','Jan 5, 2025','2025.01.05']
})
print("Original Data:\n",df)
df['Date']=pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)

#Case Normalization
import pandas as pd
df = pd.DataFrame({
    'Name':['Alice','BOB','charlie','DAVID']
})
df['Name_lower']= df['Name'].str.lower()
df['Name_upper']= df['Name'].str.upper()
print(df)

def lcs_length(X,Y):
  m,n = len(X),len(Y)
  dp = [[0]*(n+1) for _ in range(m+1)]
  for i in range(m):
    for j in range(n):
      if X[i]==Y[j]:
        dp[i+1][j+1]=dp[i][j]+1;
      else:
        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[m][n]
    seq1 = "ABCDEF"
    seq2 = "AEBDF"
    length = lcs_length(seq1,seq2)
    print(f"Longest Common Subsequence length",length)

def lcs_length(X,Y):
  m,n = len(X),len(Y)
  dp = [[0]*(n+1) for _ in range(m+1)]
  for i in range(m):
    for j in range(n):
      if X[i]==Y[j]:
        dp[i+1][j+1]=dp[i][j]+1;
      else:
        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[m][n]
    seq1 = "ACEF"
    seq2 = "AEF"
    length = lcs_length(seq1,seq2)
    print(f"Longest Common Subsequence length",length)
