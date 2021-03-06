Collected mostly from tutorials.

Plots:

- [hist.py](hist.py) Plot a histogram
- [hist2d.py](hist.py) Plot a histogram in 2d
- [kmeans.py](kmeans.py) Find the K means and plot.
- [pca.py](pca.py) Do Principal Component Analysis of the data and plot the 3 principal components.
- [plot_3d.py](plot_3d.py) Plot functions in 3d

Generators (gen/):

- [random_normal.py](gen/random_normal.py) Generate random data (1 feature, normal distribution)
- [blobs.py](gen/blobs.py) Generate random blobs (n features)

Example Usage:

- Generate test data

    python gen/blobs.py > test.csv

- Find the optimal k

    python kmeans.py test.csv

- Plot k means with chosen k

    python kmeans.py -k 4 test.csv

- Plot the principal components (Up to 3)

    python pca.py test.csv

Resources:

* https://mubaris.com/2017/10/01/kmeans-clustering-in-python/
* https://plot.ly/ipython-notebooks/principal-component-analysis/
