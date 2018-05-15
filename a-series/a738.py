while True:
    try:
        a, b = [int(i) for i in input().split()]
    except EOFError:
        break
    while a and b:
        if a > b:
            a, b = b, a
        b = b % a
    print(a)