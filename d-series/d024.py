while True:
    try:
        s = [int(i) for i in input().split()]
    except EOFError:
        break
    while s[0] and s[1]:
        if s[0] > s[1]:
            s[1], s[0] = s[0], s[1]
        s[1] = s[1] % s[0]
    print(s[0])

