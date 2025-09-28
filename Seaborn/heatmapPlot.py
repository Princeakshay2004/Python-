import seaborn as sns
import matplotlib.pyplot as mplt
import pandas as pd


anagrams=sns.load_dataset("anagrams")

anagrams.drop(columns="attnr",inplace=True)
sns.heatmap(anagrams.head(5),annot=True)
mplt.show()