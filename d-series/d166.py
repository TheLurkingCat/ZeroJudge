a = input()
while not a == '-1':
    a = [int(x) for x in a.split()]
    length = len(a)
    ans = [0] * length
    for i in range(length):
        c = 0
        for j in range(length):
            if ans[j]:
                continue     
            if c == a[i]:
                ans[j] = str(i+1)
                break
            c += 1
    print(' '.join(ans))
    try:
        a = input()
    except EOFError:
        break