import seaborn as sns
import matplotlib.pyplot as mplt
import pandas as pd



Dataframe_1={
    "name":['akshay','jivan','shivaji','vilas','vinay','suraj','suman','rakesh','ramesh'],
    "age":[21,56,23,43,65,78,12,34,56],
    "marks":[45,65,87,89,39,78,69,77,96]
    }

df=pd.DataFrame(Dataframe_1)


sns.scatterplot(x="name",y="age",hue="marks",data=df,palette="Accent")
mplt.show()