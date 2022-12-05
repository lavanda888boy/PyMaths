# in this exercise we are going to work with the radical function
# and its approximations
import matplotlib.pyplot as plot
import numpy as np


def function(x):
    return np.sqrt(x + 1)


# first of all let us define its domain and range
x_data = np.linspace(-1, 1, 1000)
y_data = list()
for i in range(0, len(x_data)):
    y_data.append(function(x_data[i]))


# for the minimax approximation we will use Chebyshev polynomials
# the degree should be seven and the most accurate points
# will be chosen automatically
cheb_coefficients = np.polynomial.chebyshev.chebinterpolate(lambda x: np.sqrt(x + 1), 7)


# function for Chebyshev interpolating polynomial
def chebyshev_polynomial(x1, degree, coefs):
    result = 0
    for j in range(0, degree):
        result += coefs[j] * pow(x1, j)

    return result


cheb_data = list()
for i in range(0, len(x_data)):
    cheb_data.append(chebyshev_polynomial(x_data[i], len(cheb_coefficients), cheb_coefficients))


# then we will try to interpolate the function
# using the method of evenly spaced points
# the task requires the polynomial of degree seven
# therefore we will have to obtain eight points
# the ends of the interval plus 6 more points
even_data = np.linspace(-1, 1, 8)
even_values = list()
for i in range(0, len(even_data)):
    even_values.append(function(even_data[i]))


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


# function for the obtained interpolating polynomial of seventh degree
def Newton_polynomial(x1, a, b, c, d, e, f, g, h):
    return a * pow(x1, 7) + b * pow(x1, 6) + c * pow(x1, 5) + d * pow(x1, 4) + e * pow(x1, 3) \
        + f * pow(x1, 2) + g * x1 + h


# and the range of the Newton's polynomial
# the number of points is six
Newton_matrix = [list(range(0, 1 + 8 * (i + 1))) for i in range(8)]
for k in range(0, len(even_values)):
    Newton_matrix[k][0] = even_values[k]

table = Newton_divided_differences(even_data, Newton_matrix, 8)

Newton_x = np.linspace(-1, 1, 1000)

# introducing polynomial coefficients (as the result of the previous operations)
a1 = 0.25937
b1 = -0.27937
c1 = -0.1392
d1 = 0.1373
e1 = 0.08738
f1 = -0.15129
g1 = 0.49956
h1 = 1.00046
Newton_y = list()
for i in range(0, len(Newton_x)):
    Newton_y.append(Newton_polynomial(Newton_x[i], a1, b1, c1, d1, e1, f1, g1, h1))


# plotting the results
plot.figure()

plot.plot(x_data, y_data, color='green', label='f = sqrt(x + 1)')

plot.plot(x_data, cheb_data, color='black', label='Chebyshev (near-minimax) method')

plot.plot(Newton_x, Newton_y, color='blue', label='Evenly spaced points')

plot.legend(loc='upper left')

plot.title("Approximating radical function", color='red', fontsize=15)
plot.xlabel("Ox", fontsize=14, color='yellow')
plot.ylabel("Oy", fontsize=14, color='yellow')

plot.grid()
plot.show()


