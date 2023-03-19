# numnpy is a python library.
# numpy is used to work with arrays
# numpy is short form of numerical python
# it also has working function with linear algerbra, fourier transformation, matrices
# exceution of arrays is 50% much more faster than traditional python
# the array object in numpy is called ndarray
# it is written in c and c++
# to install numpy : pip install numpy

import numpy as np
arr= np.array([1,2,3,4,5,6,7,8,9])
print(type(arr))


# 0-D array

a=np.array(24)
print(a)

# 1-D array
arr = np.array([1,2,3,4,5])
print(arr)
print(arr[1])

# 2-D array
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[1,1])  # this will print the value 5 from second bracket


# 3-D array

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr[1,0,1])
print(a.ndim)  # .ndim is to show the dimesion of arrays
print(arr.ndim)