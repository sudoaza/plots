import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import myplots

# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="Data CSV file")
parser.add_argument("-k","--means", type=int, help="K, number of means to pick")
parser.add_argument("-u","--upto", type=int, help="Search K up to this number", default=20)
args = parser.parse_args()


def cluster(data, k):
    # Initializing KMeans
    kmeans = KMeans(n_clusters=k)
    # Fitting with inputs
    kmeans = kmeans.fit(data)
    # Predicting the clusters
    labels = kmeans.predict(data)
    # Getting the cluster centers
    means = kmeans.cluster_centers_
    return labels, means


def find_k(data, up_to=20):
    errors = []
    for x in range(2, up_to):
        labels, means = cluster(data, x)
        # Get the distance between the data point and its closest centroid
        dist = np.linalg.norm(data-means[labels])
        errors.append(dist)
    plt.plot(errors)
    plt.show()

# Open file
data = pd.read_csv(args.csv_file).as_matrix()

if args.means:
    # find kmeans if we have k
    labels, means = cluster(data, args.means)
    myplots.scatter(data, labels=labels, markers=means)
else:
    find_k(data, args.upto)
