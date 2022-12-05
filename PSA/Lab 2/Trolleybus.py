import random

n = 10000
jora_payment = 0
for i in range(0, n):
    sum = 0
    offenses = list()
    offenses.append(0)
    index = 0
    of = 0
    for j in range(1, 2 * 365):
        if random.uniform(0, 1) <= 0.02:
            sum += 2
        elif random.uniform(0, 1) <= 0.05:
            of += 1

        offenses.append(of)
        index += 1

        if(of == 1) and (offenses[index - 1] != of):
            sum += 50
        elif (of == 2) and (offenses[index - 1] != of):
            sum += 100
        elif (of > 2) and (offenses[index - 1] != of):
            sum += 150

    jora_payment += sum

print(f"Jora has to pay {round(jora_payment / n)} lei per year")
print(f"We as the students have to pay {2 * 365 * 2} lei")
