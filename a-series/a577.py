while True:
    try:
        a = int(input())
    except EOFError:
        break
    b = int(input())
    print(a*b)
