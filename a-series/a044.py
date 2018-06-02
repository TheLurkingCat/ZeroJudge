while True:
    try:
        a = int(input())
    except EOFError:
        break
    print((1 + a) * (a * a - a + 6) // 6)
