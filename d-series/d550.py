a, b = [int(x) for x in input().split()]
out = []
for _ in range(a):
    out.append([int(x) for x in input().split()])
out.sort()
for x in out:
    print(*x)
