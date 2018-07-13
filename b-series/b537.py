from fractions import Fraction


def f(s, m):
    if m == 1 and not s & (s - 1):
        return 1 << (s - 1)
    elif s > m:
        return 2 * f(s - m, m)
    elif (s < m):
        return 1 + f(m, s)


while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    x = Fraction(a, b)
    print(f(x.numerator, x.denominator))
