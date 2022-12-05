def xnor(a, b):
    return (a and b) or (not a and not b)


print("Enter the values for xnor expression: ")
var1 = int(input())
var2 = int(input())
print(xnor(var1, var2))

