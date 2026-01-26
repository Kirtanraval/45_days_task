import pandas as pd
import numpy as np
from numpy.random import randn

data = randn(25, 8)
rows = ["a", "b", "c", "d", "e",
        "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o",
        "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y"]
cols = ["1", "2", "3", "4", "5", "6", "7", "8"]
df = pd.DataFrame(data, index=rows, columns=cols)
print(df)