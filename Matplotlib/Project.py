import matplotlib.pyplot as mplt
import pandas as pd
import numpy as np
import seaborn as sns




# To read data from csv file
Dataframe1=pd.read_csv('Diwali Sales Data.csv', encoding_errors="ignore")

# To see Head and Tail of data
print(Dataframe1.head())
print(Dataframe1.tail())


#To see Info of data 
print(Dataframe1.info())

# To remove null colums
Dataframe1.drop(columns=['Status','unnamed1'], errors='ignore',inplace=True)
print(Dataframe1.info())

# To see null values 
null_values=pd.isnull(Dataframe1).sum()
print(null_values)

# To remove null values from data
Dataframe1.dropna(inplace=True)
print(Dataframe1.info())


# To use countPlot For visulize the count of observation
sns.set_theme(style="darkgrid")
ax=sns.countplot(x="Gender" ,data=Dataframe1,palette="Accent")
for container in ax.containers:
    ax.bar_label(container)
mplt.show()

# To visulize the conut of observation on age based with male and female difference
sns.countplot(x="Age Group",hue="Gender",data=Dataframe1)
mplt.show()

#To visulize the Sales by state using barplot
sales_state=Dataframe1.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(8)
mplt.figure(figsize=(10,5))
sns.barplot(x='State',y='Amount',data=sales_state,palette="Accent",hue='State',legend=False)
mplt.show()


#To see conutplot of Occupation of Observations
mplt.figure(figsize=(13,5))
sns.set_theme(style="darkgrid")
ax=sns.countplot(x='Occupation',data=Dataframe1,palette="Accent",hue="Gender")
# Add count labels on bars
for container in ax.containers:
    ax.bar_label(container)
mplt.show()


