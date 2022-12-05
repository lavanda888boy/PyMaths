import random
import matplotlib.pyplot as plot

# we are dealing with the uniform distribution
n = 1000
frequencyList = list()
for i in range(0, 31):
    frequencyList.append(0)

for i in range(0, n):
    count = 0
    for j in range(1, 101):
        coin = random.randint(0, 1)
        if coin == 1:
            count += 1
    if 35 <= count <= 65:
        frequencyList[count - 35] += 1

# creating the graph and the structures which will build its basis
graph = plot.figure(figsize=(10, 5))


# plotting the bar graph
plot.bar(range(35, 66), frequencyList, color='blue', width=0.5)
plot.xlabel("Experiments")
plot.ylabel("Number of heads")
plot.title("Tossing the coin")
plot.show()
