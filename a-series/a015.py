"""Numpy solution
from numpy import array, savetxt
from sys import stdout

while True:
    try:
        a = [int(x) for x in input().split()]
    except EOFError:
        break
    b = []
    for _ in range(a[0]):
        b.append([int(x) for x in input().split()])
    b = array(b)
    savetxt(stdout,b.T,fmt='%i')
"""

while True:
    try:
        a = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = ''
    b = []
    for _ in range(a[0]):
        b.append([int(x) for x in input().split()])
    for i in range(a[1]):
        for j in range(a[0]):
            ans += str(b[j][i]) + " "
        ans = ans[:-1] + '\n'
    print(ans)
