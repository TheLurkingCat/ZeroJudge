from fractions import Fraction
while True:
    try:
        s = input().split()
    except EOFError:
        break
    a = Fraction(int(s[0]), int(s[1]))
    b = Fraction(int(s[2]), int(s[3]))
    if s[4] == '+':
        print(a+b)
    elif s[4] == '-':
        print(a-b)
    elif s[4] == '*':
        print(a*b)
    else:
        print(a/b)