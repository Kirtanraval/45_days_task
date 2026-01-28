import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(500, 4), columns=['A', 'B', 'C', 'D'])
df.plot(kind='scatter', x='A', y='B', c='C', title='Scatter Plot of A vs B', colormap='magma', s=50, alpha=0.6)
plt.show()