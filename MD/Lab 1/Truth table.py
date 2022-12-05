# returns the cartesian product of two sets
from itertools import product

exp = input("Write down your logical expression: ")

# list for the variables from the expression
varList = list()

# set for checking if the symbol of the expression is a variable
varSet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z'}

# filling up the list of variables
for i in range(0, len(exp)):
    if (exp[i] in varSet) and not (exp[i] in varList):
        varList.append(exp[i])

# adapting the expression for the eval() function
exp = exp.replace('!', ' NOT ')
exp = exp.replace('*', ' AND ')
exp = exp.replace('+', ' OR ')

# generating the values for the logical expression
values = list(product([0, 1], repeat=len(varList)))


# function which replaces the variables with the current values and finds its value
def evaluate(lis, expression, index):
    j1 = 0
    for k1 in range(0, len(expression)):
        for z in range(0, len(varList)):
            if expression[k1] == varList[z]:
                expression = expression.replace(expression[k1], str(lis[index][j1]))
                j1 += 1
    return eval(expression.lower())


# adapting the expression for the output
expcpy = ""
for i in range(0, len(exp)):
    expcpy += exp[i]


# printing the table
for i in range(0, len(varList)):
    print(f"| {varList[i]} ", end='')
print(f"| {exp}")

length = len(exp) + (3*len(varList)+2)
for i in range(0, length+3):
    print("-", end='')
print()

j = 0
for i in range(0, 2**len(varList)):
    for k in range(0, len(values[j])):
        print(f"| {values[j][k]} ", end='')
    print(f"| {int(evaluate(values, expcpy, j))}")
    j += 1


