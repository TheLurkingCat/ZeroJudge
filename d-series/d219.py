while True:
    try:
        a, b, c = [int(x) for x in input().split()]
    except EOFError:
        break
    print(pow(a, b, c))
