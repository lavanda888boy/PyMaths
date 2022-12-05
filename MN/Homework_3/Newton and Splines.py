# in this problem we plot two polynomial functions
# which were obtained using Newton's divided differences
# and spline interpolation methods

import matplotlib.pyplot as plot
from scipy.interpolate import CubicSpline
import numpy as np


# first we introduce Newton's divided differences
def Newton_divided_differences(x1, y1, m):
    for i1 in range(1, m):
        for j1 in range(m - i1):
            y1[j1][i1] = (y1[j1][i1 - 1] - y1[j1 + 1][i1 - 1]) / (x1[j1] - x1[i1 + j1])
    return y1


# function for printing the differences
def print_differences(y1, m):
    for i1 in range(0, m):
        for j1 in range(0, m - i1):
            print(y1[i1][j1], "\t", end=" ")
        print()


# function for the obtained interpolating polynomial of fifth degree
def Newton_polynomial(x1, a, b, c, d, e, f):
    return a * pow(x1, 5) + b * pow(x1, 4) + c * pow(x1, 3) + d * pow(x1, 2) + e * pow(x1, 1) + f


# then we define the sets of points for interpolation
x = [2, 4.5, 5.25, 7.81, 9.2, 10.6]
y = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]


# and the range of the Newton's polynomial
# the number of points is six
n = 6

Newton_matrix = [list(range(0, 1 + n * (i + 1))) for i in range(n)]
for k in range(0, len(y)):
    Newton_matrix[k][0] = y[k]

table = Newton_divided_differences(x, Newton_matrix, n)


# now we calculate the data sets for plotting the Newton's polynomial
Newton_x = np.linspace(2, 10.6, 1000)


# introducing polynomial coefficients (as the result of the previous operations)
a1 = 0.0092327
b1 = - 0.298554952
c1 = 3.68429308515
d1 = -21.442441277
e1 = 57.196254815
f1 = -46.415656367
Newton_y = list()
for i in range(0, len(Newton_x)):
    Newton_y.append(Newton_polynomial(Newton_x[i], a1, b1, c1, d1, e1, f1))


# and finally we create the corresponding cubic splines
spline = CubicSpline(x, y)
Spline_x = np.linspace(2, 10.6, 1000)
Spline_y = spline(Spline_x)

spline = CubicSpline(x, y, bc_type='clamped')
Spline_x1 = np.linspace(2, 10.6, 1000)
Spline_y1 = spline(Spline_x1)

spline = CubicSpline(x, y, bc_type='natural')
Spline_x2 = np.linspace(2, 10.6, 1000)
Spline_y2 = spline(Spline_x2)

# periodic spline is not available for our data

# plotting the results
plot.figure()

plot.plot(Newton_x, Newton_y, color='green', label='Newton interpolation')

plot.plot(Spline_x, Spline_y, color='blue', label='not-a-knot spline')
plot.plot(Spline_x1, Spline_y1, color='pink', label='clamped spline')
plot.plot(Spline_x2, Spline_y2, color='black', label='natural spline')

plot.legend(loc='upper right')

plot.plot(x, y, 'r*')

plot.title("Different interpolations", color='green', fontsize=15)
plot.xlabel("x - axis", fontsize=14, color='red')
plot.ylabel("y - axis", fontsize=14, color='red')
plot.grid()
plot.show()

# analyzing the results we can state that the natural spline
# is the one with the shortest path
