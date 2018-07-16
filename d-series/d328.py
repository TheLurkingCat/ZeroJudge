from decimal import ROUND_HALF_UP, Decimal

while True:
    try:
        s1, s2, s3 = [Decimal(x) for x in input().split()]
    except EOFError:
        break
    q = Decimal('1.00')
    ans = s1 + s2 + s3 + ((s2 * s3) / (2 * s1)) + \
        ((s3 * s1) / (2 * s2)) + ((s1 * s2) / (2 * s3))
    print(ans.quantize(q, rounding=ROUND_HALF_UP))
