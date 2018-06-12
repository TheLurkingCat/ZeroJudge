from datetime import date
while True:
    try:
        a = [int(x) for x in input().split()]
    except EOFError:
        break
    b = [int(x) for x in input().split()]
    day1 = date(*a)
    day2 = date(*b)
    x = (day1 - day2).days
    print(abs(x))
