import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(25, 4), columns=['A', 'B', 'C', 'D'])

df.abs().plot(kind='bar', title='Bar Plot of Absolute Values',stacked=True)
df.abs().plot(kind='line', title='line Plot of Absolute Values',stacked=True)
plt.show()