from math import sqrt
a = int(input())
for _ in range(a):
    x, y, z = [int(x) for x in input().split()]
    ans = (y * y) - (4 * x * z)
    if ans < 0:
        print('No')
    elif ans == 0:
        print('Yes')
    else:
        delta = sqrt(ans)
        print('Yes' if int(delta) == delta else 'No')