from datetime import date
while True:
    try:
        day1 = date(*[int(x) for x in input().split()])
    except EOFError:
        break
    day2 = date(*[int(x) for x in input().split()])
    print(abs((day1 - day2).days))
