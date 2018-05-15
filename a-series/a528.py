while True:
    try:
        a = int(input())
    except EOFError:
        break
    s = []
    for _ in range(a):
        k = int(input())
        s.append(k)
    s.sort()
    s = [str(num) for num in s]
    print('\n'.join(s))
    