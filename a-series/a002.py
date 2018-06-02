while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    print(s[0] + s[1])
