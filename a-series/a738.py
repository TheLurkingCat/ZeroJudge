from math import gcd
while True:
    try:
        a, b = [int(i) for i in input().split()]
    except Exception:
        break
    print(gcd(a, b))
