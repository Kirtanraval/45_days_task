import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
print(df)
print("conditional selection", df == "SUV")
print("conditional selection", df[df == "SUV"])
print("only for color column", df[df['BodyStyle'] == "SUV"])
print("Mixed Condition", df[(df['BodyStyle'] == "SUV") & (df['PowerTrain'] == "AWD")])
print(len(df[(df['BodyStyle'] == "SUV") & (df['PowerTrain'] == "AWD")]))
print(df[(df['BodyStyle'] == "SUV") | (df['PowerTrain'] == "AWD")][["BodyStyle","PowerTrain"]])