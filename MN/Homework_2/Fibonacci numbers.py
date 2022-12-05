import math

# Python uses IEEE double precision
# therefore we can use it for solving this problem

# computing the Fibonacci sequence
# and the errors
fibonacci = list()
fibonacci.append(1)
fibonacci.append(1)

golden_ratio = (1 + math.sqrt(5)) / 2
errors = list()
for i in range(2, 40):
    fibonacci.append(fibonacci[i-2] + fibonacci[i - 1])

for i in range(0, 39):
    errors.append(abs(golden_ratio - fibonacci[i + 1] / fibonacci[i]))

print("Fibonacci numbers    Errors")
print("---------------------------")
for i in range(0, len(fibonacci) - 1):
    print(f"{fibonacci[i]}------------------->{errors[i]}")
print(fibonacci[len(fibonacci) - 1])

# the sequence of Fibonacci numbers has linear convergence
