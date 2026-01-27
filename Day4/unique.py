import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
print(df)
print(df["Brand"])
print(df["Brand"].value_counts())
print(pd.DataFrame(df["Brand"].value_counts()))
print(pd.DataFrame(df["Brand"].unique()))
print(pd.DataFrame(np.unique(df["Brand"])))