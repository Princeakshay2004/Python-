import matplotlib.pyplot as mplt
import seaborn as sns
import pandas as pd


tips=sns.load_dataset('tips')

sns.violinplot(tips)
mplt.show()