while True:
    try:
        a = input()
    except EOFError:
        break
    temp = a[0]
    s = []
    count = -1
    for word in a:
        if temp == word:
            count += 1
        else:
            if count >= 2:
                s.append(str(count+1)+temp)
            elif count == 1:
                s.append(temp*2)
            else:
                s.append(temp)
            temp = word
            count = 0
    if count >= 2:
        s.append(str(count+1)+temp)
    elif count == 1:
        s.append(temp*2)
    else:
        s.append(temp)
    print(''.join(s))
