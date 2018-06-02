from decimal import Decimal, ROUND_HALF_UP
while True:
    try:
        a = Decimal(input())
    except EOFError:
        break
    text = a.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    if text == Decimal('-0.00'):
        text = Decimal('0.00')
    print(text)
