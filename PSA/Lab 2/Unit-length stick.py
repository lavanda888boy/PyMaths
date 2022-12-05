import random


# checks the existence of the triangle (basic inequality)
def triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return 1
    else:
        return 0


# the density function of this experiment is equal to 1/(b-a)
# the cumulative distribution function is equal to (x-a)/(b-a)
# therefore we are dealing with the uniform distribution
# X = (b-a)*rnd + a
sum = 0
for i in range(0, 1000):
    counter = 0
    for j in range(0, 1000):
        point1 = random.uniform(0, 1)
        if point1 >= 1 - point1:
            side2 = 1 - point1
            point2 = random.uniform(0, point1)
            side1 = point2
            side3 = point1 - point2
        else:
            side2 = point1
            point2 = random.uniform(point1, 1)
            side1 = point2 - point1
            side3 = 1 - point2

        if triangle(side1, side2, side3) == 1:
            counter += 1

    sum += counter / 1000


print(f"The probability of having a triangle is equal to {round(sum / 1000, 4)}")


