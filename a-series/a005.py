a = int(input())
for _ in range(a):
    s = [int(x) for x in input().split()]
    print(*s, end=' ')
    if s[1] - s[0] == s[2] - s[1]:
        print(2 * s[3] - s[2])
    else:
        print((s[3] ** 2) // s[2])
