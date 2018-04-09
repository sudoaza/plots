import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("csv_file", help="Data CSV file")
parser.add_argument("-k","--means", type=int, help="K, number of means to pick")
parser.add_argument("-u","--upto", type=int, help="Search K up to this number", default=20)
args = parser.parse_args()


pca = PCA(n_components=3)
transformed = pca.fit_transform(data)
