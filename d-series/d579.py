while True:
    try:
        a = float(input())
    except EOFError:
        break
    print('|{:.4f}|={:.4f}'.format(a, abs(a)))