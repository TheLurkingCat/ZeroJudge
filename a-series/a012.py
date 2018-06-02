while True:
    try:
        a, b = input().split()
    except EOFError:
        break
    print(abs(int(a) - int(b)))
