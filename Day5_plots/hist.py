import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

df = pd.DataFrame(randn(1000, 4), columns=['A', 'B', 'C', 'D'])
print(df)
df['A'].hist( bins=30, alpha=0.5)
plt.show()
breakpoint()