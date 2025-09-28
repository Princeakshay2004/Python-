import matplotlib.pyplot as mplt
import numpy as np
import pandas as pd
import seaborn as sns


seaborn=sns.get_dataset_names()
print(seaborn)

penguins=sns.load_dataset('penguins')
print(penguins.info())

sns.lineplot(data=penguins,x='bill_length_mm',y='bill_depth_mm',hue="sex",style="sex",size=50,palette="Accent")
mplt.show()