while True:
    try:
        a, b = (int(x) for x in input().split())
    except EOFError:
        break
    print(b+1 if a > b else b)
