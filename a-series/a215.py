"""Sympy solution, slower
from sympy import Poly, floor
from sympy.abc import x
from sympy.solvers.inequalities import solve_poly_inequality

while True:
    try:
        a, b = (int(x) for x in input().split())
    except EOFError:
        break
    left = a * (a - 1) // 2
    function = Poly((x**2 + x) - (left + b) * 2, x, domain='ZZ')
    ans = solve_poly_inequality(function, '>')
    print(floor(ans[-1].left) - a + 2)
"""
from itertools import count

while True:
    try:
        a, b = (int(x) for x in input().split())
    except EOFError:
        break
    total = ans = 0
    for x in count(a):
        total += x
        ans += 1
        if total > b:
            break
    print(ans if ans else 1)
