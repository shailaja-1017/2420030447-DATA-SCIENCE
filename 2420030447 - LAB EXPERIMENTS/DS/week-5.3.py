import pandas as pd
df=pd.DataFrame({'Color':['Red','Blue','Green','Red','Blue']})
one_hot=pd.get_dummies(df, columns=['Color'])
print("\none_hot Encoding:")
print(one_hot)