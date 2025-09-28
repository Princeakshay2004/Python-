import matplotlib.pyplot as mplt
import seaborn as sns
import pandas as pd




tips=sns.load_dataset("tips")


sns.pairplot(tips,hue="sex",palette="Accent",markers=["*","<"])
mplt.show()