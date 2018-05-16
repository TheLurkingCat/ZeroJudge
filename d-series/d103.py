while True:
    try:
        a = input()
    except EOFError:
        break
    if not a:
        break
    check = sum([int(x) * i for i, x in enumerate(a[:-2].replace('-', ''), 1)]) % 11
    if check == 10:
        check = 'X'
    else:
        check = str(check)
    if check == a[-1]:
        print('Right')
    else:
        print(a[:-1], check, sep='')