import pandas as pd
import numpy as np
stuff = {
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.choice(['dull', 'shiny'], 8),
    'D': np.random.choice([10, 20, 30, 40], 8)
}
df = pd.DataFrame(stuff)
print(df)
grouped = df.groupby(['A', 'B', 'C'])
print(grouped.sum())
print(grouped.size())
print(grouped.describe())
print(grouped.var())