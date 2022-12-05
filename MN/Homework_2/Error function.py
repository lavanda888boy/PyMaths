import matplotlib.pyplot as plot
import math

# x_args will contain the domain of our function
# and the y_args list will store its values
x_args = list()
i = -3
while i < 3:
    x_args.append(i)
    i += 0.01

y_args = list()
for j in range(0, len(x_args)):
    sum = 0
    for i in range(0, 30):
        if i % 2 == 0:
           sum += pow(x_args[j], 2 * i + 1) / ((2 * i + 1) * math.factorial(i))
        else:
            sum -= pow(x_args[j], 2 * i + 1) / ((2 * i + 1) * math.factorial(i))
    y_args.append(sum)


graph = plot.figure()
plot.plot(x_args, y_args, color='blue', linewidth=3)
plot.xlabel("Ox", color='red')
plot.ylabel("Oy", color='red')
plot.title("Taylor approximation of the error function", color='green')
plot.grid()
plot.show()

