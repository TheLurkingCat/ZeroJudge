while True:
    try:
        a = input()
    except EOFError:
        break
    s = [int(x) for x in input().split()]
    ans = [str(x) for x in sorted(s)]
    print(' '.join(ans))