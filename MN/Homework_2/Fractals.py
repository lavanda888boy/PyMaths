import numpy as np
import matplotlib.pyplot as plot

# introducing basic parameters

# the bounds for the matrix of complex numbers
x_res = 500
y_res = 500

# the bounds for the real (x) and imaginary (y) parts of complex numbers
x_min, x_max = -1, 1
y_min, y_max = -1, 1

# z_max represents the stopping criteria for finding the escape velocity
z_max = 2

# maximum number of iterations (limit)
N = 100


# function for finding the escape velocity
def escVel(z0, c, N1):
    n = 0
    z = z0
    while (abs(z) <= z_max) and (n < N1):
        z = z ** 2 + c
        n += 1

    return n


# function for printing the Julia set
def JuliaSet(z_max1, c, N1):
    # initialising an empty matrix 500 * 500 for our complex numbers
    julia_set = np.zeros((x_res, y_res))

    for iy in range(0, y_res):
        for ix in range(0, x_res):
            # mapping each pixel (matrix element) to a position of a point in the complex plane
            z = complex(ix / x_res * (x_max - x_min) + x_min, iy / y_res * (y_max - y_min) + y_min)
            julia_set[iy][ix] = escVel(z, c, N1)

    # plotting the Julia matrix using matplotlib tool imshow
    plot.imshow(julia_set, cmap='inferno')
    plot.axis('on')
    plot.title(f'z_max = {z_max1}; c = {c}; N = {N1}', fontsize=10, color='violet')
    plot.xlabel('Real part', fontsize=12, color='violet')
    plot.ylabel('Imaginary part', fontsize=12, color='violet')
    plot.show()


# the following examples were taken from the homework file
JuliaSet(1, complex(-0.835, -0.2321), N)
JuliaSet(1, complex(-0.5, 0.8), 40)
JuliaSet(1, complex(-0.79, 0.15), N)
JuliaSet(1, complex(-0.297491, 0.641051), N)
