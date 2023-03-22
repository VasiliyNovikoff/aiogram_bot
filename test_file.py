from math import factorial

n = int(input())
result = []

for i in range(n + 1):
    result.append(factorial(n) // (factorial(i) * factorial(n - i)))

print(result)
