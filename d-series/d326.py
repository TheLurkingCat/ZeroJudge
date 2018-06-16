out = []
push = out.append
while True:
    try:
        v, a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    if v < 0:
        v += 1 << 32
    k = list(format(v, 'b').zfill(32))
    k[-1-a] = str(b)
    push(''.join(k))
print(*out, sep='\n')
