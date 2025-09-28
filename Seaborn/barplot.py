import seaborn as sns
import matplotlib.pyplot as mplt
import pandas as pd



penguins=sns.load_dataset("penguins")
print(penguins.head())


print(penguins.info())

null_values=pd.isnull(penguins).sum()
print(null_values)


penguins.dropna(inplace=True)
null_values=pd.isnull(penguins).sum()
print(null_values)



sns.barplot(data=penguins,x='island',y='bill_depth_mm',hue="sex",palette="Accent")
mplt.show()
