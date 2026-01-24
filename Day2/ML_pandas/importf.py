import pandas as pd
import numpy as np

list1 = [1, 2, 3, 4, 5]
list_var = pd.Series(list1)
print("Pandas Series from list:")
print(list_var)
print(list_var[1])