import numpy as np 
arr1 = np.array([1,2,3,4,5,6,7,8,9])
x = [True, True, False, False, False, True, False, False, False]
print(arr1[x])

filtered = []
for x in arr1:
    if x % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)
print(filtered)
print(arr1[filtered])