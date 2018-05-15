while True:
    try:
        n, k = [int(x) for x in input().split()]
    except EOFError:
        break
    if n == 0 or n == k:
        print('Ok!')
    elif k == 0 or n % k:
        print('Impossib1e!')
    else:
        print('Ok!')