import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[1:4])
print(arr[:5:2])  # this will generate 1,3,5 bc it will skip 2 step 
print(arr[-4:-2])

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr[1,0:2])


# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[12,11,12]]]) print 8,9

