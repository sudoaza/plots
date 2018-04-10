import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Data CSV file")
parser.add_argument("-c","--columns", help="Columns of data to plot (two, comma separated default: 0,1)", default='0,1')
parser.add_argument("-b","--bins", type=int, help="Number of bins", default=100)
# @TODO Separate deviation into two values, one for each column
parser.add_argument("-d","--deviations", type=float, help="Keep this many times the standard deviation, used for cliping the plot.", default=3)
args = parser.parse_args()

args.columns = [int(col) for col in args.columns.split(',')]

# Open
data = pd.read_csv(args.file).as_matrix()

# Pick the column we are ploting
data = data[:, args.columns[0]:args.columns[1]+1]

mean = np.mean(data,axis=0)
sd = np.std(data,axis=0)

clip_min = mean - args.deviations * sd
clip_max = mean + args.deviations * sd

print(clip_min)
print(clip_max)
data = np.clip(data, clip_min, clip_max)

# Plot
plt.hist2d(data[:,0], data[:,1], bins=args.bins)

plt.show()
