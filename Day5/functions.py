# Applying functions to DataFrame columns
import pandas as pd
import numpy as np 
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
print(df)
# Function to calculate sum of two columns
def times(x):
    return x * 2

print(df['Range_Km'].apply(times))

# Using function to exteain the names of cars
def ext_name(name):
    if name == 'SUV':
        return 'X5'
    else:
        return name
print(df['BodyStyle'].apply(ext_name))

df['BodyStyle'] = df['BodyStyle'].apply(ext_name)
print(df)