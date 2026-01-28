import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(500, 4), columns=['A', 'B', 'C', 'D'])
df.plot(kind='hexbin', x='A', y='B', gridsize=25, cmap='magma', figsize=(8,6),xlabel='Column A', 
        ylabel='Column B', title='Hexbin Plot of A vs B')
plt.show()