# let's check the number of heads for different number of tosses
# suppose that we pay the power of two of the winning price for entering the game
import random

n = int(input("n="))
limit = int(input("limit="))
coin = 0
probability = 0
listOfMaxes = list()
index = 0
probThird = 0

# filling the special list with the probabilities higher
# or equal with a certain number (0.55)
while index <= 100:
    i = 1
    while i <= n:
        sum = 0
        thirds = 0
        for j in range(0, limit):
            counter = 0
            for k in range(0, i):
                coin = random.randint(0, 1)
            if coin == 1:
                counter += 1
            sum += counter
        probability = sum / limit
        # if (i == 3) and (probability >= 0.5):
        #    print(probability)
        if probability >= 0.55:
            listOfMaxes.append(i)
            print(probability)
        if i == 3:
            probThird += probability
        i += 1
    index += 1

print(f"The probability of winning in the 3-rd toss is {probThird / 100}")

# sorting the list of probabilities (tosses)
listOfMaxes.sort()

# finding the most frequent probability
maxFrequency = 0
indexOfMax = 0
for i in range(0, len(listOfMaxes)):
    if listOfMaxes.count(listOfMaxes[i]) > maxFrequency:
        maxFrequency = listOfMaxes.count(listOfMaxes[i])
        indexOfMax = i

# printing the results
for j in range(0, len(listOfMaxes)):
    if listOfMaxes[j] == listOfMaxes[indexOfMax]:
        print(f"On {listOfMaxes[j]}-th toss the probability of getting a head will be maximum")
        break

# checking for 10 dollars game
probability = 0
sum = 0
for k in range(0, 100):
    counter = 0
    for i in range(0, 100):
        for j in range(1, 11):
            coin = random.randint(0, 1)
        if coin == 1:
            counter += 1
    probability = counter / 100
    sum += probability

print(f"The probability of winning on 10-th toss is {sum / 100}")


# so the highest probability of winning corresponds to a 3-dollar game
# the 10- dollar game will not give us any advantage
