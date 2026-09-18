import pandas as pd
#df=pd.DataFrame({
    #'X': [10,20,30,40,50],
    #'Y': [12,24,33,45,60]
 #   'toc': [10,20,30,40,50],
  #  'ds': [12,24,33,45,60],
   # 'soa': [15,35,26,49,55]
#})
df=pd.read_csv("Iris (1).csv")
print(df.corr(method='pearson',numeric_only=float))
