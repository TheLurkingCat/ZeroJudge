from math import sqrt

while True:
    try:
        a, b, c = [int(x) for x in input().split()]
    except EOFError:
        break
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        print('Two different roots x1={} , x2={}'.format(int(
            (-b + sqrt(discriminant)) // (2 * a)), int((-b - sqrt(discriminant)) // (2 * a))))
    elif discriminant < 0:
        print('No real root')
    else:
        print('Two same roots x={}'.format(-b // (2 * a)))

"""numpy solution
from numpy import roots

while True:
    try:
        a, b = roots([int(x) for x in input().split()])
    except EOFError:
        break
    if isinstance(a, complex):
        print('No real root')
    elif a == b:
        print('Two same roots x={}'.format(int(a)))
    else:
        if a < b:
            a, b = b, a
        print('Two different roots x1={} , x2={}'.format(int(a), int(b)))
"""
