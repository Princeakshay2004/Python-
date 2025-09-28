import seaborn as sns
import matplotlib.pyplot as mplt
import array as arr
import pandas as pd
import numpy as np


penguins = sns.load_dataset("penguins")
print(penguins.head())
sns.histplot(data=penguins,x='bill_depth_mm',bins=[15,16,17,18,19,20],kde=True,)
mplt.show()
