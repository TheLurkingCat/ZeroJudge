while True:
    try:
        a = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = ''
    b = []
    for _ in range(a[0]):
        b.append([int(x) for x in input().split()])
    for i in range(a[1]):
        for j in range(a[0]):
            ans += str(b[j][i]) + " "
        ans = ans[:-1] + '\n'
    print(ans)
