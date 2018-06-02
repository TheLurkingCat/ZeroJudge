from math import factorial
a, b, k, n, m = [int(x) for x in input().split()]
print((factorial(k)//(factorial(n) * factorial(m)) * pow(a, n) * pow(b, m)) % 10007)
