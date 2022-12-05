import math

# in this problem we will apply Newton;s method of solving equations
# for that purpose we wil need to introduce the function and its derivative

# r and t represent resistance and the temperature respectively
a = 8.775468 * pow(10, -8)
b = 2.341077 * pow(10, -4)
c = 1.129241 * pow(10, -3)


def function(r, t):
    return a * pow(math.log(r, math.e), 3) + b * math.log(r, math.e) + c - 1 / t


def derivative(r):
    return (3 * a * pow(math.log(r, math.e), 2)) / r + b / r


# the precision of the root has to be 10^-5
# we will calculate R for the temperatures
# 18.99 + 273.15 and 19.01 + 273.15 Kelvin

def Newton_method(r0, t, error):
    resistance = list()
    resistance.append(r0)
    resistance.append(r0 - function(r0, t) / derivative(r0))
    index = 1
    while abs(resistance[index] - resistance[index - 1]) > error:
        resistance.append(resistance[index] - function(resistance[index], t) / derivative(resistance[index]))
        index += 1

    print(resistance[index])


print("The obtained results for 18.99 + 273.15 Kelvin and 19.01 + 273.15 Kelvin are:")
Newton_method(15000, 18.99 + 273.15, pow(10, -5))
Newton_method(15000, 19.01 + 273.15, pow(10, -5))

# the obtained range is 13066.542623383364 <= R <= 13078.426633664925

