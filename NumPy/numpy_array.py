import numpy as np

# 1D array 
one_array=np.array([1,2,3,4,5,6,7])
print(one_array)


# 2D array 
list1=np.array(([1,3,2,4,5],[2,4,5,3,5],[3,6,5,4,7]))

# To print Array
print(list1)

# To cheak the Type of Array 
print(type(list1))

# To create random  No 
list2=np.random.rand(30)
print(list2)
print(type(list2))

# To create random normal No 
numbers=np.random.normal(1,100,10)
print(numbers)

# To find mean 
list= [23,43,10,24,18]
print(np.mean(list))

# To find median
print(np.median(list))

# To find sum
print(np.sum(list))

# to sort array 
print(np.sort(list))

# Where clause 
print(np.where(one_array > 4))

# Array Slicing 
print(one_array[2:4])
