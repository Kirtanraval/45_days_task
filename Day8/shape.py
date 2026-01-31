import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(arr1)
print(np.shape(arr1))

arr2 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
print(arr2)
print(np.shape(arr2))

arr3 = np.reshape(arr1,(2,10))
print(arr3)
print(np.shape(arr3))

arr4 = np.reshape(arr1,(10,2))
print(arr4)

arr5 = np.reshape(arr1,(-1))
print(arr5)