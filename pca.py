import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import myplots

# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="Data CSV file")
parser.add_argument("-c","--components", type=int, help="Number of components to keep")
parser.add_argument("-u","--upto", type=int, help="Plot components explained variance up to this number", default=20)
args = parser.parse_args()

# Open file
data = pd.read_csv(args.csv_file).as_matrix()

# Standardizing the features
data = StandardScaler().fit_transform(data)

if args.components:
    args.components = min(args.components,data.shape[1])
    pca = PCA(n_components=args.components)
    transformed = pca.fit_transform(data)
    myplots.scatter(transformed)

else:
    args.upto = min(args.upto,data.shape[1])
    pca = PCA(n_components=args.upto)
    pca.fit(data)
    plt.plot(pca.explained_variance_)
    plt.show()
