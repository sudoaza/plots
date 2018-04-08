import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('rand.csv');

n, bins, patches = plt.hist(df['random'], 100, density=True, facecolor='g', alpha=0.75)

plt.show()
