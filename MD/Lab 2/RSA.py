import random
import math


# function, checking whether the number is prime or not
# in the for-loop there is no need to check even numbers
# and also the numbers after one half of the initial number
def is_prime(num):
    if num == 2:
        return 1
    if num < 2 or num % 2 == 0:
        return 0
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return 0
    return 1


# function for generating the pair of keys
def keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    r = (p - 1) * (q - 1)

    # randomly choosing an integer e such that e and r are relatively prime
    e = random.randint(1, r)

    # we are using Euclid's Algorithm to verify that e and r are relatively prime
    g = math.gcd(e, r)
    while g != 1:
        e = random.randint(1, r)
        g = math.gcd(r, e)

    # finding the multiplicative inverse of e modulo r
    d = pow(e, -1, r)

    # returning two tuples
    return (e, n), (d, n)


# encryption and decryption functions
def encrypt(public_key, initial_text):
    key, n = public_key
    cipher = [(ord(char) ** key) % n for char in initial_text]
    return cipher


def decrypt(private_key, cipher_text):
    key, n = private_key
    initial = [chr((char ** key) % n) for char in cipher_text]
    return ''.join(initial)


p1 = int(input("Enter a prime number: "))
q1 = int(input("Enter another prime number (Not one you entered above): "))
public, private = keypair(p1, q1)
print("Public key: ", public, " Private key: ", private)

message = input("Enter the message: ")

encrypted_message = encrypt(public, message)
print("Encrypted message: ", end='')
for i in range(0, len(encrypted_message)):
    print(encrypted_message[i], end='')
print()

print(f"Initial message: {decrypt(private, encrypted_message)}")
