import numpy as np 
arr1 = np.array([1,2,3,4,5,6,7,8,9,5])
print(arr1)
print(np.where(arr1 == 5))
print(np.where(arr1 % 2 == 0))
print(np.where(arr1 % 2 == 1))