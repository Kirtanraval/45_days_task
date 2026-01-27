# datagrab functions with pandas
import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
print(df.loc[:,'Brand'])
print("this is 1th number brand car",df.loc[1])
print("particular Row and column value :-",df.loc[2,'Brand'])