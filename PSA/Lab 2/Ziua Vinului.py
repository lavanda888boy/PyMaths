import random

# suppose that the radius if the coin is 0.25 units
# and the edge of the square is 1 unit length
counter = 0
for i in range(0, 10000):
    x = random.uniform(0, 8)
    y = random.uniform(0, 8)

    border1 = round(x)
    border2 = round(y)

    if (abs(border1 - x) > 0.25) and (abs(border2 - y) > 0.25):
        counter += 1

print(f"Probability of winning is equal to {counter / 10000}")
print("The game is not fair")

