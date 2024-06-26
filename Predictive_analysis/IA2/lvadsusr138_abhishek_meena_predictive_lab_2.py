# -*- coding: utf-8 -*-
"""LVADSUSR138_Abhishek_Meena_Predictive_Lab-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WCZ_FgM-Z4KsRVq9e8Gmr3I9DLG7moCt
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/content/Mall_Customers.csv')
df.head()

plt.scatter(df['Age'],
           df['Spending Score (1-100)'])
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')

plt.scatter(df["Spending Score (1-100)"],
            df["Annual Income (k$)"])

plt.xlabel("Spending Score (1-100)")
plt.ylabel("Annual Income (k$)")

df.isnull().sum()

columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
df = df[columns]
df.head()

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df = imputer.fit_transform(df)

scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

def find_best_clusters(df, max_k):
    centroids = []
    k_values = []

    for k in range(1, max_k):
        kmeans_model = KMeans(n_clusters=k, n_init='auto')
        kmeans_model.fit(df)

        centroids.append(kmeans_model.inertia_)
        k_values.append(k)

    return centroids, k_values

def show_elbow_plot(centroids, k_values):
    figure = plt.subplots(figsize = (12, 6))
    plt.plot(k_values, centroids, 'o-', color='orange')
    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Cluster Inertia")
    plt.title("KMeans Elbow Plot")
    plt.show()

centroids, k_vals = find_best_clusters(scaled_data, 10)
show_elbow_plot(centroids, k_vals)

k = 5
kmeans_model = KMeans(n_clusters=k, n_init='auto')
kmeans_model.fit(scaled_data)

centroids, k_vals = find_best_clusters(scaled_data, 10)
show_elbow_plot(centroids, k_vals)
k = 5
kmeans_model = KMeans(n_clusters=k, n_init='auto')
kmeans_model.fit(scaled_data)

df['cluster'] = df['cluster'].astype(int)
plt.scatter(df['Spending Score (1-100)'],
            df['Annual Income (k$)'],
            c = df['cluster'])