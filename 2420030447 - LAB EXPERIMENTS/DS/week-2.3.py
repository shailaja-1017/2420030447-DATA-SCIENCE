import pandas as pd
import numpy as np
df=pd.DataFrame({'Age': [25,30,np.nan,40,35],
                 'Department':['HR','Finance','Finance',np.nan,'IT']})
print(df)
#df_drop_rows=df.dropna()
#print("After dropping:\n",df_drop_rows)
df_drop_cols=df.dropna(axis=0)
print("After dropping:\n",df_drop_cols)