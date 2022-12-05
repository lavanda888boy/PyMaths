import random

# introducing the volume of the revolver's cylinder
n = int(input("Introduce the number of cartridges: "))

# imitating the first shot for two adjacent bullets
# supposing that they are in cartridges 1 and 2
# but it could be then used for the case without adjacent bullets

counter = 0
for i in range(0, 10000):
    shot = random.randint(1, n)
    if (shot == 1) or (shot == 2):
        counter += 1
firstShotProbability = 1 - (counter / 10000)
print(firstShotProbability)


# as we have four empty cartridges and one of them was just fired
# it means that only one out of four (4 for example) will be placed
# before the cartridge with the bullet
# so let's check the situation with no additional spinning

counter = 0
for i in range(0, 10000):
    shot = random.randint(1, n-2)
    if shot == n-2:
        counter += 1
secondShotProbability = 1 - (counter / 10000)
print(secondShotProbability)


# in this case by not spinning the cylinder
# we get a more higher probability of surviving
# because by spinning the cylinder we will get
# the initial probability
print(f"{firstShotProbability} < {secondShotProbability}")


# now let's repeat our imitations for not adjacent bullets
# we have 9 cases out of 15 of distributing the bullets in the cylinder
# when they are not adjacent:
# 6 cases for the bullets being put on the distance of one bullet
# and 3 cases for symmetrical bullets
# in both of these cases there are two empty cartridges
# which are situated before the actual bullets
# so let's calculate the probability once more

counter = 0
for i in range(0, 10000):
    shot = random.randint(1, n-2)
    if (shot == 1) or (shot == 2):
        counter += 1
thirdShotProbability = 1 - (3/15 + 6/15)*(counter / 10000)
print(thirdShotProbability)

# and again we see that it is better not to spin the cylinder
# in order to have higher surviving chances
print(f"{firstShotProbability} < {thirdShotProbability}")
