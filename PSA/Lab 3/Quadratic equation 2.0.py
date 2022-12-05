import random

# we are dealing with the equation x^2 + 4Ux + 1 = 0
# and we have to find out whether it has two distinct
# real roots or not
sum = 0
n = 10000
m = 1000
for i in range(0, n):
    probability = 0
    count = 0
    for j in range(0, m):
        u = random.uniform(0, 1)
        if 4 * (u ** 2) - 1 > 0:
            count += 1

    probability = count / m
    # print(probability)
    sum += probability

print(f"The probability of having two distinct real roots is equal to {round(sum / n, 4)}")
