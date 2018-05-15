while True:
    try:
        a = int(input())
    except EOFError:
        break
    print(a ** 2 - a + 2)