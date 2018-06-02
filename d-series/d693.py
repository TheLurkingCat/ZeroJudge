def GCD(a, b): return (GCD(b, a % b) if a % b else b)


def LCM(a, b): return (a*b//GCD(a, b))


a = int(input())
while a:
    s = [int(x) for x in input().split()]
    ans = LCM(s[0], s[1])
    while a > 2:
        ans = LCM(ans, s[a-1])
        a -= 1
    print(ans)
    a = int(input())
