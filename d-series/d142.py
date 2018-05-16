from decimal import Decimal, getcontext, ROUND_FLOOR
getcontext().prec = 1000
a = int(input())
while True:
    try:
        a = input()
    except EOFError:
        break
    if a:
        print(Decimal(a).sqrt().quantize(Decimal('1.'), rounding=ROUND_FLOOR))