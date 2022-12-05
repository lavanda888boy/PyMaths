# so we will use a large amount of random generated points in this problem
# verifying whether the sum of those randoms will reach the interval from k to n
import random

n = int(input("n="))
k = int(input("k="))
maxPts = int(input("maxPts="))


# also we find 100 varieties of all 10000 probabilities to calculate its average value
averageSum = 0
for j in range(1, 101):
    counter = 0
    for i in range(1, 10001):
        sum = 0
        while sum < k:
            sum += random.randint(1, maxPts)
        if sum <= n:
            counter += 1
    probability = counter / 10000
    averageSum += probability

print("{:.5f}".format(averageSum/100))

