a = int(input())
for _ in range(a):
    s = [int(x) for x in input().split()]
    k = [s[2] - s[0], s[3] - s[1]]
    while k[0] > 0:
        k[0] -= 1
        k[1] += 60
    if k[1] < s[4]:
        print("No")
    else:
        print("Yes")
