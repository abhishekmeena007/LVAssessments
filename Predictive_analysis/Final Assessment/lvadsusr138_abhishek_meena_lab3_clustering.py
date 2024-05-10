# -*- coding: utf-8 -*-
"""LVADSUSR138_Abhishek_Meena_Lab3_Clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CuoCffkUDkqPVlfhePZW93Az2sdy4wIL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer
import warnings

data = pd.read_csv("/content/customer_segmentation.csv")

"""exploratory data analysis"""

data.shape

data.describe()

data.info()

data.isnull().sum()

data = data.dropna(subset=['Income'])

"""selecting and extracting features"""

features = ['Year_Birth', 'Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']

X = data[features]

"""feature scaling"""

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

"""elbow and silhoutte visualizer"""

elbow_visualizer = KElbowVisualizer(KMeans(n_init=10), k=(2, 10), metric='distortion', timings=False)
elbow_visualizer.fit(X_scaled)
elbow_visualizer.show()

silhouette_visualizer = SilhouetteVisualizer(KMeans(n_clusters=elbow_visualizer.elbow_value_, n_init=10), colors='Greens')
silhouette_visualizer.fit(X_scaled)
silhouette_visualizer.show()

"""initialize K-means"""

n_clusters = elbow_visualizer.elbow_value_
kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=7)

kmeans.fit(X_scaled)

data['Cluster'] = kmeans.labels_

"""Visualization"""

plt.figure(figsize=(12, 6))
plt.scatter(data['Income'], data['MntWines'], c=data['Cluster'], cmap='viridis', alpha=0.5)
plt.xlabel('Income')
plt.ylabel('Amount spent on Wines')
plt.title('Clusters of Customers based on Income and Wine Purchases')
plt.colorbar(label='Cluster')
plt.show()