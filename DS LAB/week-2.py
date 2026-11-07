
!pip install pandas

import pandas as pd

data = {'apples' : [3,2,0,1], 'oranges' : [0,3,7,2]}
df = pd.DataFrame(data)
print(df)

import pandas as pd
data = {'apples':[3,2,0,1], 'oranges':[0,3,7,2]}
df = pd.DataFrame(data, index=['1','2','3','4'])
print(df.loc['3'])
print(df)

df = pd.read_csv('Iris.csv')
df

df.head()

df.tail()

df.head(7)

df.tail(5)

df.info()

df.shape

df = pd.read_json('airports.json')
df

import pandas as pd
df = pd.read_csv("Iris.csv")
df.shape
dup_df = pd.concat([df,df])
dup_df.shape

print(dup_df)

dup_df.drop_duplicates(inplace=True)
dup_df.shape

df.describe()

import pandas as pd
data = [1,2,3,10,20,30]
df = pd.DataFrame(data)
print(df)
df.to_csv("abc.csv",index=True)

import pandas as pd
data = {'col_1':[3,2,1,0], 'col_2':['a','b','c','d']}
pd.DataFrame.from_dict(data)

import pandas as pd
data = {'row_1':[3,2,1,0], 'row_2':['a','b','c','d']}
pd.DataFrame.from_dict(data, orient='index')

import pandas as pd
data = {'row_1':[3,2,1,0], 'row_2':['a','b','c','d']}
pd.DataFrame.from_dict(data,orient='index',columns=['A','B','C','D'])

#student rollno,name,age,section,marks of 3 different subjects(ds,cd,qc)
import pandas as pd
data = {'roll.no':[1,2,3,4,5,6,7,8,9,10], 'name':['A','B','C','D','E','F','G','H','I','J'], 'age':[18,19,20,19,18,18,19,20,18,19], 'section':[3,5,1,7,3,8,9,5,9,3], 'ds_marks':[37,70,17,16,15,10,11,47,86,90], 'cd_marks':[34,75,97,56,27,58,97,27,16,17], 'qc_marks':[65,26,16,37,89,54,37,27,85,10]}
pd.DataFrame.from_dict(data)
df.to_csv("student_info.csv",index=True)

df = pd.read_csv('Iris.csv')
df.shape
dup_df = pd.concat([df,df])
dup_df.shape
print(dup_df)
dup_df.drop_duplicates(inplace=True)
dup_df.shape
df.describe()

df = pd.read_csv('movies.csv')
#df.head()
#df.tail()
#df.info()
df.describe()

df = pd.read_csv('titanic.csv')
#df.head()
#df.tail()
#df.info()
df.describe()
