out = []
push = out.append
while True:
    try:
        a = input()
    except EOFError:
        break
    if '#' in a:
        push('{} {} {}'.format(*bytes.fromhex(a[1:])))
    else:
        push('#{:02X}{:02X}{:02X}'.format(*(int(x) for x in a.split())))
print(*out, sep='\n')
