import numpy as np
list=[1,2,3,4,5,6,7,8,9,10]
# slicing in list
print(list[2:5])

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# slicing in numpy
print(np1[2:5])

# 2d array slicing
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(np2[1:3,1:4])

# slicing till end
l = np.array([1,2,3,4,5,6,7,8,9,10])
print(l[2:])
print(l[::2])
print(l[::3])