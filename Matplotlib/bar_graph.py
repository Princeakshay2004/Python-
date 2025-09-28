import matplotlib.pyplot as mplt
import numpy as np
import pandas as pd

#matplotlib with numpy 
students=np.array(['Akshay','Jivan','Sudarshan','Vinay'])
marks=np.array([89,97,78,90])



mplt.bar(students,marks,color='green',label='Students Marks')
mplt.legend()

mplt.show()



