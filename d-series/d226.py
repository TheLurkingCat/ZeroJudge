while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    print(2*s[0]*s[1])
