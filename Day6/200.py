import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
print(df[df['TopSpeed_KmH'] > 200])