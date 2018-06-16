output = []
push = output.append
while True:
    try:
        w, x, y, z, k = [int(x) for x in input().split()]
    except EOFError:
        break
    y -= w
    z -= x
    w = x = 0
    y = abs(y)
    z = abs(z)
    if w + x + k >= y + z:
        push('die')
    else:
        push('alive')
print(*output, sep='\n')
