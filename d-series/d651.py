from decimal import Decimal, ROUND_HALF_UP
while True:
    try:
        a = Decimal(input())
    except EOFError:
        break
    k = Decimal(a.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
    print(k if k else '0.00')