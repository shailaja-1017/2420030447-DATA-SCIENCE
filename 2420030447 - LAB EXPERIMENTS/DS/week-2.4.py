import pandas as pd
df=pd.DataFrame({'ID':[1,2,2,3,4,4],
                 'Age': [25,30,30,35,40,40],
                 'Department':['alice','bob','bob','charlie','david','david']})
print(df)
df_exact=df.drop_duplicates()
print("After dropping:\n",df_exact)