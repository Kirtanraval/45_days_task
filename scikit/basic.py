import sklearn,pandas as pd,numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
# print(iris.data)
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['Target'] = iris.target
print(df)