import random
from slowprint.slowprint import *

# creating the patterns and the initial list of cells
# rule 110 (01101110 in binary)
ca = [[1, 1, 1], [1, 0, 0], [0, 0, 0]]

# rule 60 (00111100 in binary)
sierpinski = [[1, 1, 1], [1, 1, 0], [0, 0, 1], [0, 0, 0]]

cells = list()
# for the rule 110
# for i in range(1, 121):
#    cells.append(random.randint(0, 1))


# for the rule 60
for i in range(1, 61):
    cells.append(0)
cells.append(1)
for i in range(1, 61):
    cells.append(0)

# for i in range(1, 120):
#    cells.append(0)
# cells.append(1)


# function for printing the model of the cells' generation
def printGeneration(gen):
    for index in range(0, len(gen)):
        if gen[index] == 1:
            print('⬛', end='')
        else:
            print('⬜', end='')
    slowprint('', 3)


# calculating the generations assuming that the missing parents
# for the first and the last cells are zeros
printGeneration(cells)
prevGen = cells
for i in range(1, 120):
    middleGeneration = list()
    middleGeneration.append(0)

    for k in range(0, len(prevGen)):
        middleGeneration.append(prevGen[k])

    middleGeneration.append(0)

    nextGen = list()
    for j in range(1, len(middleGeneration) - 1):
        parents = [middleGeneration[j - 1], middleGeneration[j], middleGeneration[j + 1]]
        if parents in sierpinski:
            nextGen.append(0)
        else:
            nextGen.append(1)

    printGeneration(nextGen)
    prevGen = nextGen
