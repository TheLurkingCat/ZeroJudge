while True :
    try:
        s = input().split()
    except EOFError:
        break
    odd, even = 0, 0
    for group in s:
        serial = int(group[0: group.index(":")])
        r = float(group[group.index(":")+1:])
        if serial & 1:
            odd += r
        else:
            even += r
    print(odd-even)