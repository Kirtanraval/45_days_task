import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(25, 4), columns=['A', 'B', 'C', 'D'])
df.plot(kind='box')
plt.show()