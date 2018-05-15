while True:
    try:
        a = input()
    except EOFError:
        break
    s = [int(x) for x in input().split()]
    s.sort()
    output = [str(x) for x in s]
    print(' '.join(output))
    for i, num in enumerate(s):
        if num >= 60:
            if i:
                print(s[i-1])
                print(num)
            else:
                print('best case')
                print(num)
            break
    else:
        print(s[-1])
        print('worst case')