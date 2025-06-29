import numpy as np
from scipy import stats

x = np.array([6.2, 2.4, 3.2, 1.9, 0.8])
y = np.array([3.5, 4.7, 5.6, 2.1, 3.2])
z = np.array([6.2, 5.0, 6.9, 7.2, 8.5])

H, p = stats.kruskal(x, y, z)
print("H = ", H)
print("p-value = ", p)