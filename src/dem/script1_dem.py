"""
Description:
First benchmark in DEM using simple python script.
Dimensionless normal force versus dimensionless normal overlap in the linear
spring‐ dashpot model for various normal coefficients of restitutions

Software:
Basic python, pytoml for reading data

Results:
You can find the results at ~/Dropbox/Phd/results/
"""
import pytoml as toml


class Particle:
    def __init__(self, x, y, radius, u, v):
        self.x = x
        self.y = y
        self.radius = radius
        self.u = u
        self.v = v
        self.fx = 0.
        self.fy = 0.


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_forces(p, x_wall, kn=3.):
    dist = abs(p.x - x_wall)
    overlap = p.radius - dist
    if overlap > 0.:
        pass


def main():
    with open('script1_dem.toml', 'rb') as fin:
        data = toml.load(fin)

    # define the particle which will collide with rigid wall
    x = 3. * data.radius
    p = Particle(x=x, y=0., radius=data.radius, u=-1., v=0)

    t = data.tf
    dt = data.dt

    # define wall position
    x_wall = 0.

    # calulate stiffness and damping coefficient


    while t > 0:
        find_forces(p, x_wall)
        t = t - dt
        pass
    pass
