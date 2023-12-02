import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
from scipy.interpolate import griddata

roots = genfromtxt('bifurcationDiagrams/bifurcationData.csv', delimiter=',')

xi = np.linspace(min(roots[:,0]), max(roots[:,0]), 100)
yi = np.linspace(min(roots[:,1]), max(roots[:,1]), 100)
xi, yi = np.meshgrid(xi, yi)

zi = griddata((roots[:,0], roots[:,1]), roots[:,2], (xi, yi), method='linear')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xi,yi,zi, cmap='viridis')
ax.set_xlabel('beta3', fontsize=14)
ax.set_ylabel('beta4', fontsize=14)
ax.set_zlabel('Long-Term Susceptible Population', fontsize=14)
ax.set_title('Stability of the Susceptible Population as Parameters beta3 and beta4 are Changed', fontsize=16)
plt.show()