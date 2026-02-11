import sklearn,pandas as pd,numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,MinMaxScaler
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
print(df.head)
replace = df['PowerTrain']
LabelEncoder = LabelEncoder()
replace = LabelEncoder.fit_transform(replace)
print({'PowerTrain':pd.Series(replace)})

replace1 = df['RapidCharge']
OneHotEncoder = OneHotEncoder()
replace1 = OneHotEncoder.fit_transform(replace1.values.reshape(-1, 1)).toarray()
print({'RapidCharge':(replace1)})

he = OneHotEncoder()
rc = pd.DataFrame(he.fit_transform(df[['RapidCharge']]).toarray())
print(rc)

mm = MinMaxScaler()
model = pd.DataFrame(mm.fit_transform(df[['AccelSec']]))
print(model.shape,model.rename(columns={0:'AccelSec'}))