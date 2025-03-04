# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:03:22 2025

@author: Moreb
"""

import pandas as pd

# Load the dataset
dataset = pd.read_csv("/Users/Moreb/Downloads/archiveeee/IRIS.csv")

print(dataset.head())

# Check the shape of the dataset
print(dataset.shape)

# Display data types
print(dataset.dtypes)

# Summary statistics
print(dataset.describe())

import seaborn as sns
import matplotlib.pyplot as plt

# Pair plot to visualize relationships
sns.pairplot(dataset, hue='species')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Encode species
label_encoder = LabelEncoder()
dataset['species'] = label_encoder.fit_transform(dataset['species'])

# Split the dataset
X = dataset.drop('species', axis=1)  # Features
y = dataset['species']                # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

# Create a Decision Tree Classifier
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

# Classification report
print(classification_report(y_test, y_pred))

# Example prediction
sample_data = [[5.0, 3.5, 1.6, 0.6]]  # Sample features
predicted_species = model.predict(sample_data)
predicted_label = label_encoder.inverse_transform(predicted_species)
print(f'The predicted species is: {predicted_label[0]}')
