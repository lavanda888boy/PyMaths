import math

# first of all we simulate fixed point iteration
x0 = 0.1
x_args = list()
x_args.append(x0)

errors = list()
for i in range(1, 11):
    x_args.append(math.cos(x_args[i - 1]) - 1 + x_args[i - 1])
    errors.append(abs(x_args[i] - x_args[i - 1]))

convergence = list()
for i in range(1, len(errors)):
    convergence.append(errors[i] / errors[i - 1])


print("Fixed point iteration:")
print("n   xn                    xn - xn-1             rate of convergence")
print("-------------------------------------------------------------------")
print(f"{0}   {x0}")
for i in range(1, 11):
    if i < 2:
        print(f"{i}   {x_args[i]}   {errors[i - 1]}")
    else:
        print(f"{i}   {x_args[i]}   {errors[i - 1]}   {convergence[i - 2]}")


# in this case the convergence (lambda tends to 0.95) is linear
# and it is slower than the bisection method
# now let's try to use Aitken's extrapolation formula
x_args = list()
x_args.append(x0)

index = 0
for i in range(0, 3):
    x = x_args[index]
    x1 = math.cos(x) - 1 + x
    x2 = math.cos(x1) - 1 + x1

    x_args.append(x1)
    x_args.append(x2)

    coefficient = (x2 - x1) / (x1 - x)
    x3 = x2 + (coefficient * (x2 - x1)) / (1 + coefficient)

    x_args.append(x3)
    index += 3

x_args.append(math.cos(x3) - 1 + x3)

errors = list()
for i in range(1, len(x_args)):
    errors.append(abs(x_args[i] - x_args[i - 1]))

convergence = list()
for i in range(1, len(errors)):
    convergence.append(errors[i] / errors[i - 1])

print()
print()
print("Aitken's extrapolation:")
print("n   xn                    xn - xn-1             rate of convergence")
print("-------------------------------------------------------------------")
print(f"{0}   {x0}")
for i in range(1, 11):
    if i < 2:
        print(f"{i}   {x_args[i]}   {errors[i - 1]}")
    else:
        print(f"{i}   {x_args[i]}   {errors[i - 1]}   {convergence[i - 2]}")

# in this case the speed of convergence increases
