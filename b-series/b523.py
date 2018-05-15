words = set()
while True:
    try:
        a = input()
    except EOFError:
        break
    if a in words:
        print('YES')
    else:
        print('NO')
        words.add(a)