from math import gcd

while True:
    try:
        ans = gcd(*(int(i) for i in input().split()))
    except EOFError:
        break
    print(ans)
