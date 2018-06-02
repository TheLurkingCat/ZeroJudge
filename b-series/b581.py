a = int(input())
for _ in range(a):
    s = 0
    for x in input().split():
        s += int(x)
    print(s)
