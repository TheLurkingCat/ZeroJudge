from math import sqrt, floor
while True:
    try:
        a = int(input())
    except EOFError:
        break
    if a:
        a *= 2
        k = floor(sqrt(a))
        print(k)
    else:
        print(0)
