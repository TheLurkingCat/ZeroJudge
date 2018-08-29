"""Numpy solution
from numpy import array, array_split
from numpy.linalg import solve

c = int(input())
for _ in range(c):
    y = array([int(x) for x in input().split()]).reshape(2, 3)
    a, b = array_split(y, 2, axis=1)
    x = solve(a, b.flatten()).astype(int)
    print(*x)
"""

c = int(input())
for _ in range(c):
    a, b, c, d, e, f = (int(x) for x in input().split())
    delta = a * e - b * d
    delta_x = c * e - b * f
    delta_y = a * f - c * d
    x = delta_x // delta
    y = delta_y // delta
    print(x, y)
