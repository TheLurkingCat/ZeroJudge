from decimal import Decimal
while True:
    try:
        t1, t2, t3, x1, x3 = [Decimal(x) for x in input().split()]
    except EOFError:
        break
    x2 = (t2-t3) * (x1-x3) / (t1-t3)
    print('{:.6f}'.format(x2+x3))