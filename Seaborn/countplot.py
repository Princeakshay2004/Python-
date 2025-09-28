import matplotlib.pyplot as mplt
import seaborn as sns
import pandas as pd 


tips=sns.load_dataset('tips')

sns.countplot(x='sex',data=tips,hue="smoker",palette="bwr")
mplt.show()