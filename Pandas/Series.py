import pandas as pd

Data=(1,2,3,4,5)

series1=pd.Series(Data)  #It used to set data in one dimentional array called a series
print(series1)

series1[0]='Akshay'

print(series1)