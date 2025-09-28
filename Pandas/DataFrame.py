import numpy as np
import pandas as pd

dict1 ={
    "name":['Akshay','Jivan','Sudarshan','Subham'],
     "marks":[22,32,43,12],
     "city":['GKD','PUNE','LTR','KOP']
}

df= pd.DataFrame(dict1)  # Used to Convert it Into Spreadsheet

print(df)    # To print DataFrame

df.to_csv('Demo.csv',index=False)  # To convert it into Excle Spreadsheet

df.head(2)   # Shows First two rows

df.tail(3)   # Shows Last Three Rows



df1=pd.DataFrame(np.random.rand(250,9))
print(df1)
df1.to_csv("Random.csv")
df1[0][0]='Akshay'
print(df1)



df1.drop([0],inplace=True)
print(df1.max)
df1.describe
print(df1)


