import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array(arr1)
arr2[0] = 100
arr1[0] = 200
print(arr1)
print(arr2)

arr3 = np.array([0,1,2,3,4,5,6,7,8,9])
# print(arr3[::2]) # step size 2
arr4 = np.copy(arr3)
arr3[0] = 100
print(arr3)
print(arr4)