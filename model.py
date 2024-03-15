from sklearn.cluster import KMeans
import pandas as pd

def model(df):
    # Select suitable columns for K-means clustering
    X = df[['Time', 'Amount']]

    # Initialize and fit K-means model
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)

    # Get the labels assigned to each data point
    labels = kmeans.labels_

    # Count the number of records in each cluster
    cluster_counts = pd.Series(labels).value_counts()

    # Save the number of records in each cluster to a text file
    cluster_counts.to_csv('k.txt', header=False, index=False)

