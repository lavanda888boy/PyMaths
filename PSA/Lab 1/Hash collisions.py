# library with hash functions
# we need to implement md5 algorithm from it
import hashlib

# these two libraries will help us generate a random string
import random
import string


# set for storing pieces of strings
setOfHashes = set()

# list for storing hashed strings
listOfHashes = list()

print("Process in process.....")
i = 0
while i < 1:
    # generating a random 10 bytes string of letters (upper and lowercase) and digits
    line = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # hashing random strings
    # the string is encode to bytes before hashing
    hashString = hashlib.md5(line.encode())
    listOfHashes.append(hashString.hexdigest())

    # checking for collision of the first 10 HEX characters
    boofer = ''
    for j in range(0, 10):
        boofer += hashString.hexdigest()[j]
    if boofer in setOfHashes:
        print("Collision found for: " + boofer)
        i += 1
    else:
        setOfHashes.add(boofer)


# printing the results
pos = 1
for i in range(0, len(listOfHashes)):
    if listOfHashes[i].startswith(boofer):
        print(f"{pos}-hacked hash: " + listOfHashes[i])
        pos += 1
print('"V" znachit vzloman')
