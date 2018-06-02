while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    k = (s[0] * 2 + s[1]) % 3
    if k == 0:
        print("普通")
    elif k == 1:
        print("吉")
    else:
        print("大吉")
