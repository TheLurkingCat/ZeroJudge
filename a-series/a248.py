from decimal import Decimal, getcontext, ROUND_FLOOR
getcontext().prec = 100000
while True:
    try:
        a, b, c = [Decimal(x) for x in input().split()]
    except EOFError:
        break
    c = Decimal('.{}1'.format('0'*(int(c)-1)))
    print((a/b).quantize(c, rounding=ROUND_FLOOR))
