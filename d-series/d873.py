while True:
    try:
        a = input()
    except EOFError:
        break
    print(a)
    result = eval(a)
    x, y, z = a.split()
    if int(x) > 2147483647 or int(x) < -2147483648:
        print('first number too big')
    if int(z) > 2147483647 or int(z) < -2147483648:
        print('second number too big')
    if result > 2147483647 or result < -2147483648:
        print('result too big')