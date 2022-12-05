import random

# sum1, counter1 are variables for checking whether the solutions are real
# sum2, counter2 are variables for checking whether the solutions are positive
# the distribution is uniform
sum1 = 0
sum2 = 0
for i in range(0, 1000):
    counter1 = 0
    counter2 = 0
    for j in range(0, 1000):
        B = random.uniform(-1, 1)
        C = random.uniform(-1, 1)

        if B**2 - 4*C >= 0:
            counter1 += 1
            if (C > 0) and (B < 0):
                counter2 += 1

    sum1 += counter1 / 1000
    sum2 += counter2 / 1000

print(f"The probability of having two real solutions is equal to {round(sum1 / 1000, 4)}")
print(f"The probability of having two positive solutions is equal to {round(sum2 / 1000, 4)}")
