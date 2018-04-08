import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs

# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f","--features", type=int, help="Number of features", default=3)
parser.add_argument("-s","--samples", type=int, help="Number of samples", default=1000)
parser.add_argument("-g","--groups", type=int, help="Number of groups", default=4)
args = parser.parse_args()

# Creating a sample dataset with clusters
X, y = make_blobs(n_samples=args.samples, n_features=args.features, centers=args.groups)
df = pd.DataFrame(X)

# Show
print(df.to_csv(index=False))
