while True:
    try:
        a = input()
    except EOFError:
        break
    b = input()
    c = format(int(a, 2) + int(b, 2), 'b')
    print(a)
    print(b)
    print('---------------------------------')
    print('{:0>32}'.format(c))
    print('****End of Data******************')
