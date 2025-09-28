import scipy.linalg as salg
import numpy as np

# From given equation find the valllue of x and y 

# 2x-4y=18
# 5x+5y=60


a=np.array([[2,-4],[5,5]])
b=np.array([[18],[60]])


solution=salg.solve(a,b)
print(solution)