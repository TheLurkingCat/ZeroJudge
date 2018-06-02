while True:
    try:
        a, b, c = [int(x) for x in input().split()]
    except EOFError:
        break
    x, y = divmod(a, b)
    ans = str(x) + '.'
    for i in range(c):
        if y == 0:
            ans += '0'
        else:
            y *= 10
            x, y = divmod(y, b)
            ans += str(x)
    print(ans)
