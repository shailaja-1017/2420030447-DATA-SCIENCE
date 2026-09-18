import pandas as pd

# Your data dictionary
#data = {
 #   'apples': [3, 2, 0, 1],
 #   'oranges': [0, 3, 7, 2]
#}

# Correct DataFrame creation
#df = pd.DataFrame(data, index=['Ahmad', 'Ali', 'Rashed', 'Hamza'])

# Access Ali's row
#print(df.loc['Ali'])
#df = pd.read_csv('Iris (1).csv')
#df.head()
##df.info()
#print(df.shape)
#dup_df=pd.concat([df,df])
#Sdup_df.drop_duplicates(inplace=True)
#print(dup_df.shape)
#print(df.describe())
data=[1,2,3,10,20,30]
df=pd.DataFrame(data)
df.to_csv('student.csv',index=True)
#
#print(df)

data={'RollNo':[1,2,3,4,5,6,7,8,9,10], 'Age':[19,18,17,19,18,19,18,19,20,20],'Sec':['a','a','a','b','c','a','b','b','c','c'],'QC':[98,99,100,97,95,98,96,95,98,94],'DS':[100,99,98,94,100,95,94,97,98,99]}
print(pd.DataFrame.from_dict(data,orient='index',columns=[1,2,3,4,5,6,7,8,9,10]))