import numpy as np
arr1 = np.array([9,3,5,6,2,5,9,0,4])
print("Numeric arr:-")
print(f"normal arr{arr1}")
print(f"sorted arr{np.sort(arr1)}\n")

print("Alphabetical arr:-")
arr2 = np.array(['PAPU','CHUHU','PAPA','LULU','AAKA'])
print(f"normal arr{arr2}")
print(f"sorted arr{np.sort(arr2)}\n")

print("Boolean arr:-")
arr3 = np.array([True , False , True , False , True])
print(f"normal arr{arr3}")
print(f"sorted arr{np.sort(arr3)}")