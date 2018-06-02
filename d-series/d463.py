while True:
    try:
        a = int(input())
    except EOFError:
        break
    print(round(a ** (1 / 3)))
