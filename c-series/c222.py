while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    print(a ^ b)
