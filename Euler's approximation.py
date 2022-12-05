import matplotlib.pyplot as plot
import math


# first of all we define the differential equation
# y' = 6 * x^2 - 3 * x^2 * y
def y_function(x1, y1):
    return 6 * x1 * x1 - 3 * x1 * x1 * y1


# creating the graph and the structures which will build its basis
graph = plot.figure(figsize=(10, 5))
plot.xlabel("X")
plot.ylabel("Y")
plot.title("Euler's approximation")

# the real value of the function is:
value = 2 + math.pow(math.e, -1)

# initial step of approximation
h = 1
while h >= 0.001:
    # here are the two lists containing the arguments and the values of the function
    list_of_xs = list()
    list_of_ys = list()
    x = 0
    y = 3
    list_of_xs.append(x)
    list_of_ys.append(y)
    if h == 0.01:
        while x < 1:
            y += h * y_function(x, y)
            list_of_ys.append(y)
            x += h
            list_of_xs.append(x)
    else:
        while x <= 1 - h:
            y += h * y_function(x, y)
            list_of_ys.append(y)
            x += h
            list_of_xs.append(x)
    # printing the results and errors
    error = abs(value - y)
    print(f"h = {h} ---> y(1) = {round(y, 4)} ---> error = {error}")
    plot.plot(list_of_xs, list_of_ys)
    h /= 10

plot.grid()
plot.show()
