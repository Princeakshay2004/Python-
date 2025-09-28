import matplotlib.pyplot as mplt
import numpy as np


score=np.array([33,45,23,75,60,54,78,21,33,55,80,91,73])

mplt.hist(score,bins=5,color='grey',edgecolor='black')
mplt.xlabel(" Score Records")
mplt.ylabel("No of students")
mplt.title('Score Distributaion Of Students ')
mplt.show()