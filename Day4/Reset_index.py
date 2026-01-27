import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small_with_colors.csv')
df["colors"] = np.random.choice(['Red', 'Blue', 'Green'], size=len(df))
print(df.set_index('colors', inplace=True))
print("After resetting the index:")
df.reset_index(inplace=True)
df.drop(columns=['colors'], inplace=True)
print(df)
print(df['Brand'])
print(df.head(5))