while True:
    try:
        print(format(int(input()), 'b'))
    except EOFError:
        break