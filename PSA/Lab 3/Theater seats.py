import random

# the following code simulates the process of choosing the seats
sum = 0
for i in range(0, 1000):
    seats = list()
    for ind in range(0, 101):
        seats.append(0)

    count = 0
    for j in range(0, 100):
        person = random.randint(1, 100)
        if person == 1:
            count += 1
        else:
            seats[person] = 1
            for k in range(2, 100):
                if seats[k] == 1:
                    new_seat = random.randint(1, 100)
                    while seats[new_seat] == 1:
                        new_seat = random.randint(1, 100)

            if seats[len(seats) - 1] == 0:
                count += 1

    sum += count / 100

print(f"The probability that the last person will take his/her assigned seat is equal to: {round(sum / 1000, 4)}")
