while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    n = a * (a + 1) // 2
    m = b * (b + 1) // 2
    print(n * m)