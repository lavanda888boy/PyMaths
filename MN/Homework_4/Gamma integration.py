# this task requires studying Gamma function
# and the corresponding integral for computing it
from scipy import integrate, special
from numpy import linspace
import math
import warnings


# it is more convenient to ignore the accuracy warnings occurring
# while using the built-in integration methods
warnings.filterwarnings('ignore')


def Gamma_function(t, parameter):
    return pow(t, parameter - 1) * pow(math.e, -t)


# first up let us apply the built in integration methods
# we will use Gaussian quadrature method
print('Gaussian quadrature deviation:')
x = 1
while x <= 4:
    value = integrate.quadrature(lambda t: pow(t, x - 1) * pow(math.e, -t), 0, x)
    print(f'x = {x}; relative_error = {round(abs(value[0] - special.gamma(x)) / special.gamma(x), 5)}')
    x += 0.25
print()
print()


# secondly we apply composite Simpson's rule
print('Composite Simpson method deviation:')
x = 1
while x <= 5:
    x_args = linspace(1, 10, 1000)
    y_args = list()
    for i in range(0, len(x_args)):
        y_args.append(Gamma_function(x_args, x))

    value = integrate.simps(y_args, x_args)
    print(f'x = {x}; relative_error = {round(abs(value[0] - special.gamma(x)) / special.gamma(x), 5)}')
    x += 0.25
print()
print()


# also we can try to use general purpose quadrature method
# and see the error in the integration itself
print('General purpose quadrature method deviation and calculation error:')
x = 1
while x <= 4:
    value = integrate.quad(lambda t: pow(t, x - 1) * pow(math.e, -t), 0, x)
    print(f'x = {x}; integral_error = {value[1]}; relative_deviation = {round(abs(value[0] - special.gamma(x)) / special.gamma(x), 5)}')
    x += 0.25
print()
print()


# as we can see from our results the smallest errors are provided by
# the composite Simpson's method; the rule is better to use for x values
# especially from 2 to 4 because at that interval the deviation is bounded
# and is decreasing; at the same time for the general purpose quadrature method
# it is permanently increasing and the error in computing the integral is
# not stable; it is also important to mention that the Gaussian quadrature
# method provides us with the bounded deviation on the interval from 1 to 2;
# also, both first and the third methods show smaller ratio of the errors
#  when x is increasing;
