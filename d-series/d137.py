while True:
    try:
        a = input().replace('i', 'j')
    except EOFError:
        break
    a = abs(complex(a))
    print('{:.3f}'.format(a))