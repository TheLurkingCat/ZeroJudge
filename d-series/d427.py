from decimal import Decimal, getcontext, ROUND_FLOOR, InvalidOperation
getcontext().prec = 1000
while True:
    try:
        a = input()
    except EOFError:
        break
    try:
        print(Decimal(a).sqrt().quantize(
            Decimal('1E-50'), rounding=ROUND_FLOOR))
    except InvalidOperation:
        print(a)
