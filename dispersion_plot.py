import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-np.pi/2, np.pi/2, 2000)
y = np.linspace(-np.pi/2, np.pi/2, 2000)

X, Y = np.meshgrid(x, y)

def omega(x, y):
    return np.sqrt(np.sin(x)**2 + np.sin(y)**2)

z = omega(X, Y)

ax.contour3D(2*X/np.pi, 2*Y/np.pi, z,50)
ax.set_xlabel(r'$p_x/a$')
ax.set_ylabel(r'$p_y/a$')
ax.set_zlabel(r'$\omega/B$')
ax.set_title("3D Contour plot of dispersion relation in 1st Brillouin Zone")
plt.show()



