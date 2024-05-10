# -*- coding: utf-8 -*-
"""LVADSUSR138_Abhishek_Meena_Lab1_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Be6CjpG4wd4gM8H2nrHIT6ZT1UJOHezr
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
import matplotlib.pyplot as plt

data = pd.read_csv("/content/Fare prediction.csv")

data.shape

data.describe()

data.info()

"""check for null values"""

data.isnull().sum()

print("Number of duplicate rows:", data.duplicated().sum())
data = data.drop_duplicates()
print("Number of duplicate rows after dropping duplicates:", data.duplicated().sum())

"""exploratory data analysis"""

plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['fare_amount']])
plt.title('Box Plot of Fare Amount (Before Outlier Removal)')
plt.show()

"""encoding the data"""

label_encoder = LabelEncoder()
data['key'] = label_encoder.fit_transform(data['key'])
data['pickup_datetime'] = label_encoder.fit_transform(data['pickup_datetime'])

X = data[['key', 'pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']]
y = data['fare_amount']

"""model training and testing"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

"""model evaluation metrics"""

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mse)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)

"""scatter plot for Actual vs Predicted Fare"""

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.55)
plt.xlabel('Actual Fare Amount')
plt.ylabel('Predicted Fare Amount')
plt.title('Actual vs. Predicted Fare Amount using linear regression')
plt.show()