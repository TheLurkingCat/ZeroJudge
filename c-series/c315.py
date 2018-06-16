a = int(input())
pos = [0, 0]
for _ in range(a):
    x, y = [int(x) for x in input().split()]
    if x == 0:
        pos[1] += y
    elif x == 1:
        pos[0] += y
    elif x == 2:
        pos[1] -= y
    else:
        pos[0] -= y
print(*pos)
