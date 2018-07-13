while True:
    try:
        a = list(input().lower())
        backup = a.copy
    except EOFError:
        break
    for i, word in enumerate(a):
        if word == ' ':
            continue
        else:
            c = backup()
            c[i] = c[i].upper()
            print(*c, sep='')
