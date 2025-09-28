import matplotlib.pyplot as mplt
import numpy as np



x=np.arange(5)
y=np.array([5,3,6,4,8])
mplt.plot(x,y,c='g',marker='.',label='Sales in 2025',linestyle=":")

mplt.xlabel("Days")
mplt.ylabel("Slales")
mplt.grid()
mplt.title("Sales of week !")
mplt.legend()
mplt.xticks(x,['M1','M2','M3','M4','M5'])

mplt.show()
