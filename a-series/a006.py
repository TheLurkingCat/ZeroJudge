while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    a, b, c = s
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        print('Two different roots x1={} , x2={}'.format(int(
            (-b + discriminant ** 0.5) // 2 * a), int((-b - discriminant ** 0.5) // 2 * a)))
    elif discriminant < 0:
        print('No real root')
    else:
        print('Two same roots x={}'.format(int(-b/(2*a))))
