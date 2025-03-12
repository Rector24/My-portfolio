# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 10:51:11 2025

@author: Moreb
"""

import pandas as pd

# Load the dataset
dataset = pd.read_csv("/Users/Moreb/Downloads/advertising.csv")

# Display the first few rows of the dataset
print(dataset.head())

# Check for missing values
print(dataset.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

# Pairplot to visualize relationships
sns.pairplot(dataset)
plt.show()

from sklearn.model_selection import train_test_split

# Define features and target
X = dataset[['TV', 'Radio', 'Newspaper']]
y = dataset['Sales']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

