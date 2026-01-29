import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')
x , y = [df[['AccelSec']], df['TopSpeed_KmH']]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Mean Square Error:",mean_squared_error(y_test, y_pred))
print("R2 Score:",r2_score(y_test, y_pred))
print("Mean Absolute Error:",mean_absolute_error(y_test, y_pred))
import matplotlib.pyplot as plt
for i in range(len(X_test)):
    plt.plot([X_test.iloc[i], X_test.iloc[i]],[y_test.iloc[i], y_pred[i]],color='gray', alpha=0.4)
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', marker='x', label='Predicted')
plt.plot(X_test, y_pred, color='green')
plt.xlabel('AccelSec')
plt.ylabel('TopSpeed_KmH')
plt.title('Error Visualization')
plt.legend()
plt.show()