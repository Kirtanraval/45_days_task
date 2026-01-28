import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Data = load_diabetes()
df = pd.DataFrame(data=Data.data, columns=Data.feature_names)
df['target'] = Data.target  #we need to add target column as well to the dataframe to make it complete ans use for regression tasks.
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training data shape:", X_train.shape , y_train.shape)
print("Testing data shape:", X_test.shape , y_test.shape)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Predictions on test set:", predictions.shape)
# Evaluate the model
# Calculate R^2 score, Mean Squared Error, Mean Absolute Error, and Intercept
# R^2 score helps us understand how well our model explains the variance in the target variable and Higher R^2 values indicate better model performance.
r2 = model.score(X_test, y_test)
print("R^2 score on test set:", r2)
# Mean Squared Error (MSE) and Mean Absolute Error (MAE) provide insights into the average prediction error of the model and lower values indicate better performance.
mse = np.mean((predictions - y_test) ** 2)
print("Mean Squared Error on test set:", mse)
mae = np.mean(np.abs(predictions - y_test))
print("Mean Absolute Error on test set:", mae)
# Model Intercept helps us understand the baseline value of the target variable when all features are zero.
intercept = model.intercept_
print("Model Intercept:", intercept)

# Visualize Actual vs Predicted values
plt.scatter(y_test, predictions)
plt.xlabel("Actual Target Values")  
plt.ylabel("Predicted Target Values")
plt.title("Actual vs Predicted Target Values")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, color='red')
plt.show()