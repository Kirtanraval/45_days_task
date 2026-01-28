import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(25, 4), columns=['A', 'B', 'C', 'D'])
print(df)
df.plot(kind='area', stacked=False)
df.abs().plot(kind='area', alpha=0.2 , title='Area Plot with Transparency', legend=True, fontsize=12)
df[['A', 'B']].plot(kind='bar', stacked=True, title='Stacked Bar Plot', legend=True, fontsize=12)
df[['C', 'D']].abs().plot(kind='pie', stacked=False, title='Horizontal Bar Plot', legend=True, fontsize=12, subplots=True , layout=(1,2), figsize=(10,5),table=True)   
plt.show()