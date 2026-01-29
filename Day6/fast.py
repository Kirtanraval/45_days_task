import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
df['PowerTrain'] = df['PowerTrain'].astype('category').cat.codes
X = df[['AccelSec', 'Range_Km', 'PowerTrain']]
y = df['TopSpeed_KmH']
model = LinearRegression()
model.fit(X, y)
df['PredictedSpeed'] = model.predict(X)
fast_predicted = df[df['PredictedSpeed'] > 200]
print(fast_predicted[['Brand', 'Model', 'PredictedSpeed']])
df.plot(kind='scatter', x='AccelSec', y='PredictedSpeed', title='Predicted Speed vs Acceleration Time')
plt.show()
