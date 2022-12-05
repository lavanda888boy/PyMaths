# import class for operating with images
from PIL import Image
import random

img = Image.open('danger_zone.png')

# generating random pixels from the map to check
# the frequency of the red ones appearing
sum = 0
for i in range(1, 6):
    reds = 0
    for j in range(0, 3200*1530):
        x = random.randint(1, 3200-1)
        y = random.randint(1, 1530-1)
        if img.getpixel((x, y)) == (255, 0, 0, 255):
            reds += 1
    print(f"{i} check passed")
    probability = reds / (3200*1530)
    sum += probability

print(f"The area of the mined land is equal to {round((sum / 5) * 42, 4)} square miles")
