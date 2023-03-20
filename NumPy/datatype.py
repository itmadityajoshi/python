#string , integer, float, bollean, complex etc are the datatypes of numpy
# i=> integer, b=> boolean, u=>unsigned integer, f=> floate, c =>complex float
# m = timedelta, M=>datetime, O =<Object, s=>string, u=>unicode string
#fixed chunk of memory for others data type (void)


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.dtype)

myarr=np.array([1,2,3,4,5], dtype= 'S')
print(myarr)
print(myarr.dtype)


#shape
s=np.array([[1,2,3],[4,5,6]])
print(s.shape)  # it shows the matix type 2*3 , 3*3  etc

#reshape
arr=np.array([1,2,3,4,5,6,7,8,9])
newarr=arr.reshape(3,3)
print(newarr)
