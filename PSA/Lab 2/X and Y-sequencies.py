import random
import matplotlib.pyplot as plot

expectedCash = 0
n = 10
cash = list()
while n <= 1000000:
    for i in range(0, n):
        X = random.uniform(0, 1)
        Y = random.uniform(0, 1)

        j = 2
        while Y <= X:
            Y = random.uniform(0, 1)
            j += 1

        expectedCash += j - 2
    cash.append(expectedCash / n)
    n *= 10

# creating the graph and the structures which will build its basis
graph = plot.figure(figsize=(20, 5))

# plotting the bar graph
plot.plot([10, 100, 1000, 10000, 100000, 1000000], cash, color='blue', marker='o')
plot.xlabel("Tries")
plot.ylabel("Expected cash")
plot.title("Experiment with sequences")
plot.show()

# the expected value is always increasing therefore
# there can be paid any fee to enter the game
