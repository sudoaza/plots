import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", type=file, help="Data CSV file")
args = parser.parse_args()

# Open
df = pd.read_csv(args.file)

# Plot
n, bins, patches = plt.hist(df['random'], 100, density=True, facecolor='g', alpha=0.75)

plt.show()
