while True:
    try:
        a = int(input())
    except EOFError:
        break
    text = dict()
    num = 1
    for _ in range(a):
        k = input()
        try:
            print('Old!', text[k])
        except KeyError:
            text[k] = num
            print('New!', num)
            num += 1
