while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    del s[0]
    avg = sum(s) / len(s)
    print('no' if avg > 59 else 'yes')
