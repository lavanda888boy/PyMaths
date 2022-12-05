# in this exercise we will be working with Gamma function

import matplotlib.pyplot as plot
from scipy.special import gamma
from scipy.interpolate import CubicSpline
import numpy as np
import math

# first of all we introduce the data set
n = [1, 2, 3, 4, 5]
data = [1, 1, 2, 6, 24]
log_data = [0, 0, math.log(2, math.e), math.log(6, math.e), math.log(24, math.e)]


# the we will create Newton's interpolating polynomial
# using Newton's divided differences
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


# function for the obtained interpolating polynomial
def Newton_polynomial(x1, a, b, c, d, e):
    return a * pow(x1, 4) + b * pow(x1, 3) + c * pow(x1, 2) + d * pow(x1, 1) + e


Newton_matrix = [list(range(0, 1 + 5 * (i + 1))) for i in range(5)]
for k in range(0, len(data)):
    Newton_matrix[k][0] = data[k]

table = Newton_divided_differences(n, Newton_matrix, 5)


# now we calculate the data sets for plotting the Newton's polynomial
Newton_x = np.linspace(1, 5, 1000)


# introducing polynomial coefficients (as the result of the previous operations)
a1 = 0.375
b1 = -3.417
c1 = 11.627
d1 = -16.587
e1 = 9.002
Newton_y = list()
for i in range(0, len(Newton_x)):
    Newton_y.append(Newton_polynomial(Newton_x[i], a1, b1, c1, d1, e1))


# similarly we create logarithmic polynomial
# function for the logarithmic interpolating polynomial
def Logarithmic_polynomial(x1, a, b, c, d, e):
    return pow(math.e, a * pow(x1, 4) + b * pow(x1, 3) + c * pow(x1, 2) + d * pow(x1, 1) + e)


logarithmic_matrix = [list(range(0, 1 + 5 * (i + 1))) for i in range(5)]
for k in range(0, len(data)):
    logarithmic_matrix[k][0] = log_data[k]

table = Newton_divided_differences(n, logarithmic_matrix, 5)

# now we calculate the data sets for plotting the logarithmic polynomial
log_x = np.linspace(1, 5, 1000)


# introducing logarithmic coefficients
a1 = 0.007079126
b1 = -0.118738272
c1 = 0.882025072
d1 = -1.921094202
e1 = 1.150728276
log_y = list()
for i in range(0, len(log_x)):
    log_y.append(Logarithmic_polynomial(log_x[i], a1, b1, c1, d1, e1))


# then we create the corresponding cubic spline for our function
spline = CubicSpline(n, data, bc_type='natural')
Spline_x = np.linspace(1, 5, 1000)
Spline_y = spline(Spline_x)


# finally we create data sets for plotting gamma function itself
gamma_x = np.linspace(1, 5, 1000)
gamma_y = gamma(gamma_x)


# plotting the results
plot.figure()

plot.plot(Newton_x, Newton_y, color='green', label='Newton interpolation')

plot.plot(Spline_x, Spline_y, color='blue', label='natural spline')

plot.plot(log_x, log_y, color='yellow', label='Logarithmic interpolation')

plot.plot(gamma_x, gamma_y, color='violet', label='Gamma plot')

plot.legend(loc='upper left')

plot.plot(n, data, 'r*')

plot.title("Gamma function", color='violet', fontsize=15)
plot.xlabel("x - axis", fontsize=14, color='green')
plot.ylabel("y - axis", fontsize=14, color='green')

plot.grid()
plot.show()


# our final task is to compute the accuracy of all three approximations
def max_error(start, end, array, test_array):
    max = abs(array[0] - test_array[0])
    index = start + 1
    while index < end:
        if abs(array[index] - test_array[index]) > max:
            max = abs(array[index] - test_array[index])
        index += 1

    return max


max_Newton = max_error(0, len(gamma_y), gamma_y, Newton_y)
max_spline = max_error(0, len(gamma_y), gamma_y, Spline_y)
max_logarithmic = max_error(0, len(gamma_y), gamma_y, log_y)

print("Maximum error of each method:")
print(f"Newton's method: {max_Newton}")
print(f"Cubic spline: {max_spline}")
print(f"Logarithmic approximation: {max_logarithmic}")

# so finally we can conclude that using logarithmic method to
# approximate Gamma function is the most accurate way
