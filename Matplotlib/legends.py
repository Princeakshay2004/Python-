import matplotlib.pyplot as mplt
import numpy as np

x=np.arange(5)
y1=np.array([10,23,43,53,67])
y2=np.array([11,23,45,67,51])

mplt.plot(x,y1,'--b',c="r",label='Frequency')
mplt.plot(x,y2,label='Periods')

mplt.legend(loc='lower center')

mplt.show()