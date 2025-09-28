import matplotlib.pyplot as mplt
import numpy as np

Fruits=np.array(['Apple','mango',"Banana",'Lemon','Avacodo'])
Quentity=np.array([78,96,45,34,55])

mplt.pie(Quentity,labels=Fruits,autopct='%1.1f%%')
mplt.title("Fruits Stock Avlable")
mplt.show()