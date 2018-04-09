import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Data CSV file")
args = parser.parse_args()

# Open
df = pd.read_csv(args.file).as_matrix()

# Plot
n, bins, patches = plt.hist(df[:,0], 100, density=True, facecolor='g', alpha=0.75)

plt.show()
