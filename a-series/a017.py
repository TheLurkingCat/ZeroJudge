while True:
    try:
        print(eval(input().replace('/', '//')))
    except EOFError:
        break
