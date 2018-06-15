while True:
    x = []
    y = []
    push_x = x.append
    push_y = y.append
    try:
        a = [int(x) for x in input().split(',')]
    except EOFError:
        break
    for num in a:
        if num & 1:
            push_x(str(num))
        else:
            push_x('{}')
            push_y(num)
    y.sort()
    print(','.join(x).format(*y))
