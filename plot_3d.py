from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def s_ts_sum(x):
  return sigmoid(np.tanh(x) + sigmoid(x))

def t_ts_mul(x):
  return np.tanh(np.tanh(x) * sigmoid(x))

def sum_n_mul(x):
  return np.tanh(s_ts_sum(x) + t_ts_mul(x))

fig = plt.figure(figsize=plt.figaspect(0.333))

x = np.linspace(-1.0, 1.0, 50)
y = np.linspace(-1.0, 1.0, 50)
X, Y = np.meshgrid(x, y)


ax = fig.add_subplot(2, 3, 1, projection='3d',title='tanh')
Z = np.tanh(X+Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

ax = fig.add_subplot(2, 3, 2, projection='3d',title='sigmoid')
Z = sigmoid(X+Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

ax = fig.add_subplot(2, 3, 3, projection='3d',title='s_ts_sum')
Z = s_ts_sum(X+Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

# ---------------------

ax = fig.add_subplot(2, 3, 4, projection='3d',title='t_ts_mul')
Z = t_ts_mul(X+Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')


ax = fig.add_subplot(2, 3, 5, projection='3d',title='sum_n_mul')
Z = sum_n_mul(X+Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')



plt.show()
