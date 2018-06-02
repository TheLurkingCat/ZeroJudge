while True:
    try:
        a = int(input())
    except EOFError:
        break
    print(*(['=_=|||'] * a), sep='\n')
