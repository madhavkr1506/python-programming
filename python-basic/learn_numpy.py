import numpy as np 
# array = np.array(8)
array = np.array([1,2,3,4,5])
array = np.array([1,2,3,4,5], ndmin = 2)
print(array[0,1])

print(array.dtype)
print(type(array))

newarr = array.copy()
print(newarr)
