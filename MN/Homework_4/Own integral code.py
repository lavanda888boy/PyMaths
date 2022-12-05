# in this exercise we will not use special python methods
# in order to apply numerical integration of different types
# but instead will use our own computer routine and develop
# some code for Simpson's rule and Gaussian quadrature
from scipy.special import legendre
import numpy as np


# the first rule finds the corresponding quadratic polynomial
# in order to bound the respective region
# a and b are the ends of the interval
# n is the number of its divisions

# it is also important to mention that we are dealing with improper
# integral of type 2 with x = 1 being the vertical asymptote
# as the function tends to infinity
# therefore we will have to integrate not exactly from 1
def function(x):
    return pow(x - 1, -5 / 2)


def Simpson_method(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    riemann_sum = (h / 3) * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return riemann_sum


# showing the results
print('Results for the Simpson method:')
N = 4
for i in range(0, 5):
    print(f'n = {N}; integral value = {Simpson_method(lambda x: function(x), 1 + 1e-8, 4, N)}')
    N *= 2


# then we apply the Gaussian quadrature which initially
# works for the interval [-1; 1]
# for that we will need to generate nodes and weights
# of the quadrature using Legendre polynomials of degree n
# their solutions will become nodes and the weights will be
# determined using the special formula
def Legendre_derivative(coefficients, degree, x):
    value = 0
    index = degree
    j = 1
    while index != 0:
        value += coefficients[j - 1] * index * pow(x, degree - j)
        j += 1
        index -= 1

    return value


# a and b are the limits of integration
def Legendre_function(a, b, t):
    return pow((b + a + t * (b - a)) / 2 - 1, -5/2)


def Gaussian_quadrature(nod, weight, a, b):
    gaussian_sum = 0
    for index in range(0, len(nod)):
        gaussian_sum += weight[index] * Legendre_function(a, b, nod[index])

    return gaussian_sum * (b - a) / 2


# the integral will be calculated by multiplying
# the corresponding nodes and weights consecutively
print()
print()
print()
print('Results for the Gaussian quadrature method:')
N = 4
for i in range(0, 5):
    coefs = list(legendre(N))
    nodes = np.roots(coefs)
    weights = list()
    for k in range(0, len(nodes)):
        weights.append(2 / ((1 - pow(nodes[k], 2)) * (Legendre_derivative(coefs, N, nodes[k])) ** 2))

    print(f'n = {N}; integral value = {Gaussian_quadrature(nodes, weights, 1, 4)}')
    N *= 2


# in conclusion I would say that the Gaussian quadrature method
# converges much faster than the Simpson's method in approaching
# to the real value of the integral, but we I also observed that
# the quadrature at first tends to infinity and later starts to
# tend to the real value; however we can state that the Gaussian
# quadrature converges as n goes to infinity
