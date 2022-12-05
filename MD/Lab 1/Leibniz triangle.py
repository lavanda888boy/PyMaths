# import class for printing fractions from module fraction
from fractions import Fraction

n = int(input("Enter the depth of the triangle: "))

# creating the matrix for triangle fractions
matrix = list()

# printing the triangle
if n == 1:
    print(Fraction(1, 1))
elif n == 2:
    print(f"   {Fraction(1, 1)}   ")
    print(f"{Fraction(1, 2)} {Fraction(1, 2)}")
else:
    # printing the first row
    for i in range(0, (4*n-1-1)//2):
        print(' ', end='')
    print(1, end='')
    for i in range(0, (4*n-1-1)//2):
        print(' ', end='')
    print()

    # printing  the second row
    for i in range(0, (4*n-1-2*3-1)//2):
        print(' ', end='')
    print(f"{Fraction(1, 2)} {Fraction(1, 2)}", end='')
    rowList = list()
    rowList.append(Fraction(1, 2))
    rowList.append(Fraction(1, 2))
    matrix.append(rowList)
    for i in range(0, (4*n-1-2*3-1)//2):
        print(' ', end='')
    print()

    # printing the rest of the triangle
    # remember that fractions take 3*n symbols on each level
    # and spaces between them take n-1 symbols
    # and there are 4*n-1 symbols in each row
    # moreover there are [(4*n-1) - 3*i - (i-1)]/2 indents from right and left
    # of each n-1 row (but I didn't take into consideration that there are longer fractions)
    # where i is the current row starting from 3
    k = 1
    for i in range(3, n+1):
        for il in range(0, (4*n-1-3*i-i+1)//2):
            print(' ', end='')

        print(f"{Fraction(1, i)} ", end='')
        rowList = list()
        matrix.append(rowList)
        matrix[k].append(Fraction(1, i))
        for j in range(1, i-1):
            print(f"{matrix[k-1][j-1] - matrix[k][j-1]} ", end='')
            matrix[k].append(matrix[k-1][j-1] - matrix[k][j-1])
        print(Fraction(1, i), end='')
        matrix[k].append(Fraction(1, i))
        k += 1

        for ir in range(1, (4*n-1-3*i-i+1)//2):
            print(' ', end='')
        print()

