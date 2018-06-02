while True:
    try:
        s = input()
    except EOFError:
        break
    temp = []
    ans = 0
    for x in s:
        if x < 'A' or x > 'z' or 'Z' < x < 'a':
            temp.append(' ')
        else:
            temp.append(x)
    k = ''.join(temp)
    print(len(k.split()))
