from decimal import Decimal, ROUND_FLOOR
while True:
    try:
        a = Decimal(input())
    except EOFError:
        break
    if 0 <= a <= 100:
        a = a * 9 / 10 + 8
    elif 100 < a <= 500:
        a = a * 8 / 10
    else:
        a = a * 6 / 10
    a = str(a)
    try:
        a = float(a[:a.index(".")+3])
    except ValueError:
        pass
    print('${:.2f}'.format(a))
