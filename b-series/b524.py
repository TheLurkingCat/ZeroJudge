while True:
    try:
        a = input()
    except EOFError:
        break
    y = 0
    ans = 0
    for i, x in enumerate(a):
        if x == 'y':
            ans += abs(i - y)
            y += 3
    print(ans)
