from operator import mul
from functools import reduce
from math import gcd
while True:
    out = []
    push = out.append
    try:
        m, k = [int(x) for x in input().split()]
    except EOFError:
        break
    s = [int(x) for x in input().split()]
    x = reduce(gcd, s)
    x *= reduce(mul, s)
    c = x
    while k + x < m:
        push(k + x)
        x += c
    print(*out)
