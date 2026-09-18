import pandas as pd
df=pd.DataFrame({'Name':['alice','BOB','charlie','DAVID']})
df['lower']=df['Name'].str.lower()
df['upper']=df['Name'].str.upper()
print(df)