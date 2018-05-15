from fractions import gcd
while True:
    try:
        a, b = [int(i) for i in input().split()]
    except EOFError:
        break
    print (gcd(a, b))
