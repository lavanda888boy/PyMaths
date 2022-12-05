import random
import math

# it is obvious that the probability of a dart landing
# in the upper half of the target is equal to 1/2 (condition)
# so let us simulate all the cases using
# using the equation of the circle x^2 + y^2 = 100

"""
# THE DART LANDS IN THE RIGHT HALF OF THE TARGET
sum = 0
n = 10000
m = 1000
for i in range(0, n):
    probability = 0
    count = 0
    for j in range(0, m):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        if (0 < x < 10) and (0 < y < 10):
            count += 1

    probability = count / m
    # print(probability)
    sum += probability

print(f"The probability of the dart landing in the right half of the target is equal to {round(sum / n, 4) * 2}")
"""

"""# ITS DISTANCE FROM THE CENTER IS LESS THAN FIVE INCHES
sum = 0
n = 10000
m = 1000
for i in range(0, n):
    probability = 0
    count = 0
    for j in range(0, m):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        if (-5 < x < 5) and (0 < y < 5):
            count += 1

    probability = count / m
    # print(probability)
    sum += probability

print(f"The probability of the dart having the distance from the center less 5 inches is equal to {round(sum / n, 4) * 2}")
"""

"""#ITS DISTANCE FROM THE CENTER IS GREATER THAN FIVE INCHES
sum = 0
n = 10000
m = 1000
for i in range(0, n):
    probability = 0
    count = 0
    for j in range(0, m):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        if ((-10 < x < -5) or (5 < x < 10)) and (5 < y < 10):
            count += 1

    probability = count / m
    # print(probability)
    sum += probability

print(f"The probability of the dart having the distance from the center greater 5 inches is equal to {round(sum / n, 4) * 2}")
"""

# ITS LANDS WITHIN 5 INCHES FROM THE POINT (0, 5)
sum = 0
n = 10000
m = 1000
for i in range(0, n):
    probability = 0
    count = 0
    for j in range(0, m):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        dist = math.sqrt(x ** 2 + (5 - y) ** 2)
        if (dist <= 5) and (0 < y < 10):
            count += 1

    probability = count / m
    # print(probability)
    sum += probability

print(f"The probability of the dart landing at the distance from the point (0, 5) within 5 inches is equal to {round(sum / n, 4) * 2}")

