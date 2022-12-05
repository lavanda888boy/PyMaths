from fractions import Fraction

# so let us calculate the mathematical expectancy
# of the described experiment for an arbitrary
# number of tosses

expectancy = 0
for n in range(1, 1000):
    expectancy += (2**(n-1)) * Fraction(1, 2**n)
    if n % 10 == 0:
        print(expectancy)

# the mathematical expectancy of winning tends to infinity
# that is why the winning price can be infinitely large
# and, moreover, it doesn't depend on the number of tosses
