import numpy as np
import matplotlib.pyplot as plt


def create_circle(radius=1, center=[0, 0], surface_points=20):
    """
    This function is used to create a dem particle with points
    on the surface with given number of surface points
    """
    rng = np.linspace(0, 2*np.pi, 20)
    x = radius * np.cos(rng)
    y = radius * np.sin(rng)

    # delete the last element as it will reconsider the point at start
    x = x[0:-1] + center[0]
    y = y[0:-1] + center[1]

    return x, y


def calculate_normals(x, y):
    normals = np.zeros((len(x), 2))

    for i in range(len(x)):
        if i is (len(x) - 1):
            dx = (x[0] - x[i-1])
            dy = (y[0] - y[i-1])
        else:
            dx = (x[i+1] - x[i-1])
            dy = (y[i+1] - y[i-1])
        magn = np.sqrt(dx**2+dy**2)
        normal = [dy/magn, -dx/magn]
        normals[i] = normal

    # plt.quiver(x, y, normals[:, 0], normals[:, 1])
    # plt.show()
    return normals


x, y = create_circle()
calculate_normals(x, y)
