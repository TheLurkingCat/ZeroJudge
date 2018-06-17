from itertools import combinations
a = int(input())
temp = []
M = 0
push = temp.append
find = temp.index
for _ in range(a):
    push([int(x) for x in input().split()])
for (x1, y1), (x2, y2) in combinations(temp, 2):
    t = pow(x1 - x2, 2) + pow(y1 - y2, 2)
    if t > M:
        M = t
        ans = (find([x1, y1]), find([x2, y2]))
print(*ans)
