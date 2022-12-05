import random
import math


# the radius of the unit circle is equal to 1/(2*pi)
# three angles between 0 and 2*pi are generated further
# the corresponding coordinates are cos(angle) for x and sin(angle) for y
# the distribution is uniform
sum = 0
for i in range(0, 1000):
    counter = 0
    for j in range(0, 1000):
        x = random.uniform(0, 2 * math.pi)
        y = random.uniform(0, 2 * math.pi)
        z = random.uniform(0, 2 * math.pi)

        l = list()
        l.append(x)
        l.append(y)
        l.append(z)
        l.sort()

        # diameter = 1 / math.pi
        if l[2] - l[0] > math.pi:
            counter += 1

    sum += counter / 1000

print(f"The probability of having a triangle with all acute angles is equal to {round(sum / 1000, 4)}")

