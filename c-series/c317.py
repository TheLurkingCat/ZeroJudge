a = int(input())
for _ in range(a):
    X, a, b = [int(x) for x in input().split()]
    i, j = divmod(X, a)
    m = i
    for __ in range(i+1):
        if not j % b:
            break
        j += a
        m -= 1
    else:
        print(-1)
        continue
    k = (X-a*m)//b
    print((X + (b-a)*m)//b)