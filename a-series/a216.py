while True:
    try:
        a = int(input())
    except EOFError:
        break
    g = 0
    for n in range(1, a):
        g += n * (n+1) // 2
    f = a * (a+1) // 2
    g += f
    print(f, g)
