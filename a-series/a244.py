N = int(input())
for _ in range(N):
    s = [int(x) for x in input().split()]
    if s[0] == 1:
        print(s[1] + s[2])
    elif s[0] == 2:
        print(s[1] - s[2])
    elif s[0] == 3:
        print(s[1] * s[2])
    else:
        print(s[1] // s[2])