while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    total = 0
    ans = 0
    for x in range(a, b):
        total += x
        ans += 1
        if total > b:
            break
    print(ans)
