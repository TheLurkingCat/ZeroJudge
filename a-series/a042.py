while True:
    try:
        a = int(input())
    except EOFError:
        break
    print(a * (a - 1) + 2)
