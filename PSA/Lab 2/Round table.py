import random
import matplotlib.pyplot as plot

n = 5
probabilities = list()
people = list()
while n <= 100:
    people.append(n)
    sum = 0
    for i in range(0, 1000):
        count = 0
        for j in range(0, 100):
            """
            r = random.randint(1, n)
            q = random.randint(1, n)
            if (abs(r - q) == 1) or (abs(r - q) == n - 1):
                r = random.randint(1, n)
                q = random.randint(1, n)
                if (abs(r - q) != 1) and (abs(r - q) != n - 1):
                    count += 1
            """
            r = random.randint(1, n)
            q = random.randint(1, n)
            r1 = random.randint(1, n)
            q1 = random.randint(1, n)
            if (abs(r - q) != 1) and (abs(r - q) != n - 1) and (abs(r1 - q1) != 1) and (abs(r1 - q1) != n - 1):
                count += 1

        sum += count / 1000
    probabilities.append(round(sum / 1000, 4))
    n += 5


graph = plot.figure(figsize=(10, 5))

# plotting the bar graph
plot.plot(people, probabilities, color='blue')
plot.xlabel("People")
plot.ylabel("Probabilities")
plot.title("Probability that no two people will sit next to each other")
plot.show()
