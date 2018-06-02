from math import ceil
a = int(input())
for _ in range(a):
    x, y, z = [int(x) for x in input().split()]
    if z >= y and x > y:
        print('Poor Snail')
    else:
        print(ceil((x-y) / (y-z)) + 1)
