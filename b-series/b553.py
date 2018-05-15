while True:
    try:
        a = int(input())
    except EOFError:
        break
    ans = 0
    while a != 1:
        if a & 1:
           a = 3 * a + 1
        else:
            a = a // 2
        ans+=1
    print(ans)