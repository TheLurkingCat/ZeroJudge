import datetime
while True:
    try:
        a = [int(x) for x in input().split()]
    except EOFError:
        break
    b = [int(x) for x in input().split()]
    day1 = datetime.date(a[0],a[1],a[2])
    day2 = datetime.date(b[0],b[1],b[2])
    x = (day1 - day2).days
    ans = str(abs(x))
    print(ans)