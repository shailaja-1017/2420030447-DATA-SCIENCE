import pandas as pd
df=pd.DataFrame({'ID':[1,2,2,3,4,4],
                 'Age': [25,30,30,35,40,40],
                 'Name':['alice','bob','bob','charlie','david','david']})
print(df)
df_subset_id=df.drop_duplicates(subset=['ID'])
print("After removal id:\n",df_subset_id)
df_subset_name=df.drop_duplicates(subset=['Name'])
print("After removal name:\n",df_subset_name)