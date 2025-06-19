# Code is for reference - from Great Learning
# It did NOT provide dataset


#K Means Clustering is an unsupervised learning algorithm used to partition a dataset into k clusters,
# where each  data point belongs to the cluster with the nearest mean.
# Scaling the data can improve the performance of clustering algorithms by equalizing the influence of
# different features.


import pandas as pd
from scipy.stats import zscore
from sklearn.cluster import KMeans
import sklearn as sk

# Read the dataset
df = pd.read_csv('data.csv')

# Scale the selected features
features = ['mpg', 'displacement', 'weight', 'acceleration']
df_scaled= df[features].apply(zscore)

print(sk.__Version__)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df_scaled)
centroids = kmeans.cluster_centers_
