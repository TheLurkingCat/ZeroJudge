while True:
    try:
        s = [x for x in input().lower() if 96 < ord(x) < 123]
    except EOFError:
        break
    flag = 0
    k = list(set(s))
    for x in k:
        if s.count(x) & 1:
            if len(s) & 1:
                flag += 1
                if flag == 2:
                    print('no...')
                    break
            else:
                print('no...')
                break
    else:
        print('yes !')
