import random
import matplotlib.pyplot as plot

n = 5
rollings = list()
probabilities = list()
while n <= 15:
    counter = 0
    for j in range(0, 10000):
        for i in range(0, n):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            dice3 = random.randint(1, 6)

            if dice1 + dice2 + dice3 == 14:
                counter += 1
                break

    rollings.append(n)
    probabilities.append(round(counter / 10000, 4))
    # print(round(s / 10000, 4))
    n += 1

# creating the graph and the structures which will build its basis
graph = plot.figure(figsize=(10, 5))

# plotting the bar graph
plot.plot(range(5, 16), probabilities, color='pink', marker='o')
plot.xlabel("Rollings")
plot.ylabel("Winning probabilities")
plot.title("Rolling the dice")
plot.show()
