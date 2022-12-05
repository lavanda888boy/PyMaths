# in this problem we will work with Fresnel integrals
# which are applied in the light diffraction
# then we will plot the obtained functions
from scipy import special, integrate
from numpy import linspace
import matplotlib.pyplot as plot
import math


# first of all we will compute their real values
# on the interval from zero to five
arguments = linspace(0, 5, 1000)
S, C = special.fresnel(arguments)

print("The numerical results for Fresnel integrals are:")
print(f"scipy.special.fresnel method: C(0:5) = {C[len(C) - 1]}; S(0:5) = {S[len(S) - 1]}")


# plotting the original accurate Fresnel functions
plot.subplot(1, 3, 1)
plot.plot(arguments, C, color='blue', label='C(x)')
plot.plot(arguments, S, color='red', label='S(x)')
plot.title('Fresnel integrals real values', color='violet', fontsize=14)
plot.xlabel('x - axis', color='green', fontsize=12)
plot.ylabel('y - axis', color='green', fontsize=12)
plot.legend()
plot.grid()


# then we use the general purpose quadrature method
def C(t):
    return math.cos(math.pi * pow(t, 2) / 2)


def S(t):
    return math.sin(math.pi * pow(t, 2) / 2)


C_quad = list()
S_quad = list()
for i in range(0, len(arguments)):
    C1 = integrate.quad(lambda x: C(x), 0, arguments[i])
    S1 = integrate.quad(lambda x: S(x), 0, arguments[i])
    C_quad.append(C1[0])
    S_quad.append(S1[0])


# plotting the obtained functions
plot.subplot(1, 3, 2)
plot.plot(arguments, C_quad, color='blue', label='C(x)')
plot.plot(arguments, S_quad, color='red', label='S(x)')
plot.title('General purpose quad method', color='violet', fontsize=14)
plot.xlabel('x - axis', color='green', fontsize=12)
plot.ylabel('y - axis', color='green', fontsize=12)
plot.legend()
plot.grid()

print(f"general purpose quadrature method: C(0:5) = {C_quad[len(C_quad) - 1]}; S(0:5) = {S_quad[len(S_quad) - 1]}")


# finally, we apply composite Simpson's rule
arguments = linspace(0, 5, 1000)
simps_C = list()
simps_S = list()
for i in range(0, len(arguments)):
    x_args = linspace(0, arguments[i], 1000)
    y_args_1 = list()
    y_args_2 = list()

    for j in range(0, len(x_args)):
        y_args_1.append(C(x_args[j]))
        y_args_2.append(S(x_args[j]))

    simps_C.append(integrate.simps(y_args_1, x_args))
    simps_S.append(integrate.simps(y_args_2, x_args))


# plotting the results
plot.subplot(1, 3, 3)
plot.plot(arguments, simps_C, color='blue', label='C(x)')
plot.plot(arguments, simps_S, color='red', label='S(x)')
plot.title('Composite Simpson method', color='violet', fontsize=14)
plot.xlabel('x - axis', color='green', fontsize=12)
plot.ylabel('y - axis', color='green', fontsize=12)
plot.legend()
plot.grid()
plot.show()


print(f"composite Simpson's method: C(0:5) = {simps_C[len(simps_C) - 1]}; ", end='')
print(f"S(0:5) = {simps_S[len(simps_S) - 1]};")
