while True:
    try:
        a = int(input())
    except EOFError:
        break
    s = []
    push = s.append
    for _ in range(a):
        k = int(input())
        push(k)
    s.sort()
    print(*s, sep='\n')
