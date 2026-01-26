import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
df.loc[0]
df.shape
df.ndim
df.dtypes
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df['Model'].value_counts(ascending=True))
print(f"{df['Model'].value_counts(normalize=True)}")
print(df.groupby('Model').count())
PriceIndia = [300000, 450000, 600000, 750000, 500000, 650000,
              700000, 800000, 1200000, 900000, 1100000, 950000,
              400000, 850000, 1050000, 1150000, 1250000, 1300000,
              1400000, 1500000, 1600000, 1700000, 1800000, 1900000,
              2000000, 2100000, 2200000, 2300000, 2400000, 2500000,
              2600000, 2700000, 2800000, 2900000, 3000000, 3100000,
              3200000, 3300000, 3400000, 3500000, 3600000, 3700000,
              3800000, 3900000, 4000000, 4100000, 4200000, 4300000,
              4400000, 4500000, 4600000, 4700000, 4800000, 4900000,
              5000000, 5100000, 5200000, 5300000, 5400000, 5500000,
              5600000, 5700000, 5800000, 5900000, 6000000, 6100000,
              6200000, 6300000, 6400000, 6500000, 6600000, 6700000,
              6800000, 6900000, 7000000, 7100000, 7200000, 7300000,
              7400000, 7500000, 7600000, 7700000, 7800000, 7900000,
              8000000, 8100000, 8200000, 8300000, 8400000, 8500000,
              8600000, 8700000, 8800000, 8900000, 9000000, 9100000,
              9200000, 9300000, 9400000, 9500000, 9600000]
df = df.iloc[:len(PriceIndia)]
df['PriceIndia'] = PriceIndia
print(df)
df['crash'] = [np.nan] * len(df)
df['crash'].iloc[::10] = 'crashed'  
print(df)
df.to_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\car_data_with_price_and_crash.csv', index=False)   
print(df)
df.insert(1, 'color' , [True] * len(df) * True)
print(df)
df.to_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\car_data_final.csv', index=True)  
print(df)
print(df.columns)
df.drop('crash', axis=1, inplace=True)
print(df)
df.drop(3, axis=0, inplace=True)
print(df)