import math
import matplotlib.pyplot as plot


# in this problem we will use Newton's method and fixed - point iteration method
# also we ill try to optimize them to increase the order of convergence

# first of all we introduce the function and its derivative


def function(x):
    return pow(math.e, x - math.pi) + math.cos(x) - x + math.pi


def derivative(x):
    return pow(math.e, x - math.pi) - math.sin(x) - 1


def second_derivative(x):
    return pow(math.e, x - math.pi) - math.cos(x)


# creating the domain and the range of the function
x_args = list()
y_args = list()
i = 0
while i < 5:
    x_args.append(i)
    y_args.append(function(i))
    i += 0.01

# plotting the graph of the function
graph = plot.figure()
plot.plot(x_args, y_args, color='red', linewidth=3)
plot.xlabel("x-axis", color='blue')
plot.ylabel("y-axis", color='blue')
plot.title("Function f", color='green')
plot.grid()
plot.show()


# now we start applying Newton's method
# our initial guess will be 2 / b or 2 / 5
# with the accuracy 10^-5
def Newton_method(x0, error):
    x_list = list()
    x_list.append(x0)
    x_list.append(x0 - function(x0) / derivative(x0))

    print("Newton's method:")
    print("n   xn                    xn - xn-1             order of convergence")
    print("---------------------------------------------------------------------")
    print(f"{0}   {x0}")
    print(f"{1}   {x_list[1]}   {x_list[1] - x0}")

    index = 1
    while abs(x_list[index] - x_list[index - 1]) > error:
        x_list.append(x_list[index] - function(x_list[index]) / derivative(x_list[index]))
        print(
            f"{index + 1}   {x_list[index + 1]}   {abs(x_list[index + 1] - x_list[index])}   {math.log(x_list[index], x_list[index + 1])}")
        index += 1

    for j in range(0, 3):
        print()


Newton_method(0.4, pow(10, -5))


# the convergence in this case is linear, because the solution
# is situated at the point where the tangent line is Ox axis
# and the derivative is equal to zero


def fixedPoint_method(x):
    return pow(math.e, x - math.pi) + math.cos(x) + math.pi


# now we will try to use fixed - point iteration method
x0 = 3
x_args = list()
x_args.append(x0)

errors = list()
for i in range(1, 21):
    x_args.append(fixedPoint_method(x_args[i - 1]))
    errors.append(abs(x_args[i] - x_args[i - 1]))

convergence = list()
for i in range(1, len(errors)):
    convergence.append(math.log(x_args[i - 1], x_args[i]))

print("Fixed point iteration:")
print("n   xn                    xn - xn-1             order of convergence")
print("---------------------------------------------------------------------")
print(f"{0}   {x0}")
for i in range(1, 21):
    if i < 2:
        print(f"{i}   {x_args[i]}   {errors[i - 1]}")
    else:
        print(f"{i}   {x_args[i]}   {errors[i - 1]}   {convergence[i - 2]}")

for j in range(0, 3):
    print()


# according to the results we can say that the order of convergence
# tends to 0.93 that is why this is the linear convergence, which is
# slower than Newton's method and highly depends on the initial guess
# which I have chosen according to the drawn graph


# if we take the derivative of the initial function and apply Newton's method
# to it, then we will have a quadratic convergence
def Newton_method_upgrade(x0, error):
    x_list = list()
    x_list.append(x0)
    x_list.append(x0 - derivative(x0) / second_derivative(x0))

    print("Newton's method upgraded:")
    print("n   xn                    xn - xn-1             order of convergence")
    print("---------------------------------------------------------------------")
    print(f"{0}   {x0}")
    print(f"{1}   {x_list[1]}   {x_list[1] - x0}")

    index = 1
    while abs(x_list[index] - x_list[index - 1]) > error:
        x_list.append(x_list[index] - derivative(x_list[index]) / second_derivative(x_list[index]))
        print(f"{index + 1}   {x_list[index + 1]}   {abs(x_list[index + 1] - x_list[index])}   {math.log(x_list[index], x_list[index + 1])}")
        index += 1

    for j in range(0, 3):
        print()


Newton_method_upgrade(4, pow(10, -5))
