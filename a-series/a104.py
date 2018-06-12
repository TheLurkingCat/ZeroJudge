while True:
    try:
        a = input()
    except EOFError:
        break
    s = [int(x) for x in input().split()]
    s.sort()
    print(*s)
