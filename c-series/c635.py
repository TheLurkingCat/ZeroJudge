from itertools import zip_longest
while True:
    out = []
    x = []
    y = []
    push_x = x.append
    push_y = y.append
    push = out.append
    try:
        a = [int(x) for x in input().split(',')]
    except EOFError:
        break
    for i, num in enumerate(a):
        if i & 1:
            push_x(num)
        else:
            push_y(num)
    x.sort()
    y.sort()
    for a, b in zip_longest(x, y):
        push(b)
        if a is not None:
            push(a)
    print(*out, sep=',')
