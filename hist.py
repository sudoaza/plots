import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Data CSV file")
parser.add_argument("-c","--column", type=int, help="Column of data to plot", default=0)
parser.add_argument("-b","--buckets", help="Number of buckets", default=100)
parser.add_argument("-d","--deviations", type=float, help="Keep this many times the standard deviation, used for cliping the plot.", default=3)
args = parser.parse_args()

# Open
data = pd.read_csv(args.file).as_matrix()

# Pick the column we are ploting
data = data[:,args.column]

mean = np.mean(data)
sd = np.std(data)

clip_min = mean - args.deviations * sd
clip_max = mean + args.deviations * sd

data = np.clip(data, clip_min, clip_max)

# Plot
n, bins, patches = plt.hist(data, args.buckets, density=True, facecolor='g', alpha=0.75)

plt.show()
