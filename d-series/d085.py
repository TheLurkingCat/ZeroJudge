"""Sympy solution
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.solvers.solvers import simplify

while True:
    try:
        n = int(input())
    except EOFError:
        break
    ans = str(simplify(sqrt(n))).replace('*', '').replace('I',
                                                          'i').replace(')', '').replace('sqrt(', '_/')
    print(ans)
"""
from math import sqrt

output = []
push = output.append
while True:

    try:
        n = int(input())
    except EOFError:
        break
    if n:
        negtive = n < 0
        n = abs(n)
        sqrt_n = int(sqrt(n))
        l = 1
        for i in range(2, sqrt_n + 1):
            t = i ** 2
            while (n % t == 0):
                l *= i
                n //= t
        temp = []
        concate = temp.append
        if l != 1:
            concate(str(l))
        if n != 1:
            concate('_/{}'.format(n))
        if negtive:
            concate('i')
        push(''.join(temp))
    else:
        push('0')
print(*output, sep='\n')
