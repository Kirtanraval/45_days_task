import pandas as pd
import numpy as np  
stuff = {
    'cars': ['BMW', 'Volvo', 'Ford', 'Honda', 'Toyota', 'Audi'],
    'passings': [3, 7, np.nan, 10, 5, 8]
}
df = pd.DataFrame(stuff)
print(df)
print(df.dropna(inplace=False))
print(df.fillna(value=0))
print(df['passings'].fillna(value=df['passings'].mean()))
print(df['passings'].fillna(value=df['passings'].max()))
print(df['passings'].fillna(value=df['passings'].min()))