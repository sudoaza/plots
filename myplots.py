import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

def scatter(data, labels=np.empty(0), markers=np.empty(0)):
    plt.rcParams['figure.figsize'] = (16, 9)
    fig = plt.figure()
    ax = Axes3D(fig)
    if labels.any():
        ax.scatter(data[:,0], data[:,1], data[:,2], c=labels)
    else:
        ax.scatter(data[:,0], data[:,1], data[:,2])
    if markers.any():
        ax.scatter(markers[:,0], markers[:,1], markers[:,2], marker='*', c='#050505', s=1000)
    plt.show()
