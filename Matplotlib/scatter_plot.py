import matplotlib.pyplot as mplt
import numpy as np


# It used to find co-relation between two varibles 
# ex, advertise & Sales
work_hours=np.array([4,6,2,8,3,9,1])
payment=np.array(work_hours*3)

mplt.scatter(work_hours,payment,label='Work_Based payment',marker='*')
mplt.legend()
mplt.grid()
mplt.xlabel("Work_Hours")
mplt.ylabel("Payment")

mplt.show()