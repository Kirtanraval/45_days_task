import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('C:\\Users\\RK\\OneDrive\\Desktop\\45_days_task\\Datasets\\small.csv')

# Encode categorical PowerTrain
df['PowerTrain'] = df['PowerTrain'].astype('category').cat.codes

# Features and target
X = df[['AccelSec', 'Range_Km', 'PowerTrain']]
y = df['TopSpeed_KmH']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Visualization
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Speed")
plt.ylabel("Predicted Speed")
plt.title("Actual vs Predicted Top Speed")
plt.show()