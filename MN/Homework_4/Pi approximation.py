# in this task we will compute the integral which approximates
# the number pi using different numerical integration methods
from math import pi
from scipy import integrate
import timeit


def pi_function(x):
    return 4 / (1 + x ** 2)


# let us start from the midpoint rule
# we are working on the interval [a, b]
# h is the step size, n - number of sub-intervals
def midpoint_rule(a, b, n):
    h = (b - a) / n
    integral_value = 0
    for i in range(n):
        integral_value += pi_function((a + h / 2.0) + i * h)

    return integral_value * h


# composite trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral_value = 0.5 * (pi_function(a) + pi_function(b))

    for i in range(1, n):
        k = a + i * h
        integral_value += pi_function(k)

    integral_value *= h

    return integral_value


# composite Simpson rule
def Simpson_rule(a, b, n):
    h = (b - a) / n

    x_args = list()
    y_args = list()

    # calculating values of x and f(x)
    i = 0
    while i <= n:
        x_args.append(a + i * h)
        y_args.append(pi_function(x_args[i]))
        i += 1

    # calculating the value of the integral
    integral_value = 0
    i = 0
    while i <= n:
        if (i == 0) or (i == n):
            integral_value += y_args[i]
        elif i % 2 != 0:
            integral_value += 4 * y_args[i]
        else:
            integral_value += 2 * y_args[i]
        i += 1

    integral_value *= (h / 3)

    return integral_value


# and now let's start to study the behaviour of each method
# by measuring the error and the time needed for computations
# we will vary the value of n for each method

start = timeit.default_timer()

print('Midpoint rule:')
N = 2
prev_error = 1
while N <= 2**21:
    experimental_value = midpoint_rule(0, 1, N)
    error = abs(pi - experimental_value)
    if N < 128:
        ratio = round(prev_error / error, 4)
        prev_error = error
        print(f'N = {N}; error = {error}; ratio = {ratio}')
    else:
        print(f'N = {N}; error = {error}')
    N *= 2

end = timeit.default_timer()
print(f'\nTotal time required: {round(end - start, 5)} seconds')
print('\n\n\n')


start = timeit.default_timer()

print('Composite trapezoidal rule:')
N = 2
prev_error = 1
while N <= 2**21:
    experimental_value = trapezoidal_rule(0, 1, N)
    error = abs(pi - experimental_value)
    if N < 128:
        ratio = round(prev_error / error, 4)
        prev_error = error
        print(f'N = {N}; error = {error}; ratio = {ratio}')
    else:
        print(f'N = {N}; error = {error}')
    N *= 2

end = timeit.default_timer()
print(f'\nTotal time required: {round(end - start, 5)} seconds')
print('\n\n\n')


start = timeit.default_timer()

print('Composite Simpson rule:')
N = 2
while N <= 2**21:
    experimental_value = Simpson_rule(0, 1, N)
    error = abs(pi - experimental_value)
    prev_error = error
    print(f'N = {N}; error = {error}')
    N *= 2

end = timeit.default_timer()
print(f'\nTotal time required: {round(end - start, 5)} seconds')
print('\n\n\n')


# we can do the same procedure with the in-built
# Gaussian quadrature routine

start = timeit.default_timer()

print('Gaussian quadrature:')
for j in range(1, 10):
    tolerance = 10 ** (-j)
    experimental_value = integrate.quadrature(lambda x: pi_function(x), 0, 1, tol=tolerance)
    error = abs(pi - experimental_value[0])
    print(f'tolerance = {tolerance}; error = {error}')

end = timeit.default_timer()
print(f'\nTotal time required: {round(end - start, 5)} seconds')


# in conclusion I would say that analyzing the elapsed time for each method
# we can state that the Gaussian quadrature routine is the most optimal
# we may also notice that the Simpson's method works pretty slow in comparison
# with the others but it is important that at the same time its error converges
# much quicker than the error in the midpoint and trapezoidal rules

# the converges I am talking about means that at a certain point of decreasing h
# the error will stop decreasing and will become approximately constant or even larger

# that's because for midpoint and trapezoidal rules we get the error formulas equal to:
# C/n^p, where 2^p = ratio = 4 and therefore p = 2, h = (b-a)/n and the obtained result is
# C*h^2 (because h = 1/n);
# for the Simpson's rule however things are a little bit different because the ratio
# does not converge to a certain value and therefore it may vary from 150 to 60
# therefore I will write the expression C*h^4 as mentioned in the lecture presentations

# it is obvious now that if we increase the value of h to the infinity the error will
# tend to zero and therefore further increasings will not be necessary

