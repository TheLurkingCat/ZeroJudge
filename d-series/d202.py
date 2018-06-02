from decimal import Decimal, getcontext
ex = Decimal('0.' + '0' * 200)
getcontext().prec = 10000
while True:
    try:
        a, b = [Decimal(x) for x in input().split()]
    except EOFError:
        break
    print((a+b).quantize(ex))
