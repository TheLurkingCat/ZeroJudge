while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    while not a == b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)
