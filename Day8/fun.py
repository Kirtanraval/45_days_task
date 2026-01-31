import numpy as np 
arr1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(arr1)
print(np.square(arr1))
print(np.absolute(arr1))
print(np.exp(arr1))
print(np.min(arr1))
print(np.max(arr1))
if (arr1 == np.sign(arr1)).all():
    print("All elements are positive",arr1[arr1>0])
elif (arr1 == -np.sign(arr1)).all():
    print("All elements are negative", arr1[arr1<0])
else:
    print("Array contains both positive and negative elements")