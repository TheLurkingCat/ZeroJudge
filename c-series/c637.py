from operator import mul
from functools import reduce

M = 0


def chinese_remainder(n, a):
    total = 0
    prod = reduce(mul, n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    k = total % prod
    return k if k > M else k+prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


out = []
push = out.append
while True:
    ans = 0
    try:
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
    except EOFError:
        break
    M = max(b)
    push(chinese_remainder(a, b))
print(*out, sep='\n')
