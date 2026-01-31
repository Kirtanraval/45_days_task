import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9]) # 1 D
for  ar in arr1:
    print(ar)


arr2 = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]) # 2 D
for  ar in arr2:
    for ar1 in ar:
        print(ar1)

arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # 3 D
for x in arr3:
    for y in x:
        for z in y:
            print(z)

arr4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # iterator for 3 D

for x in np.nditer(arr4):
    print(x)