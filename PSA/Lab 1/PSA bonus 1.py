# import class for operating with images
from PIL import Image

img = Image.open('danger_zone.png')

# counting the number of red pixels on the image
reds = 0
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if img.getpixel((i, j)) == (255, 0, 0, 255):
            reds += 1

# finding the total area of red pixels
mapArea = 42

# the size of the image is 3200*1530 pixels
redArea = (reds / (img.size[0]*img.size[1])) * mapArea

print(f"The area of mined land is equal to {round(redArea, 4)} square miles")

