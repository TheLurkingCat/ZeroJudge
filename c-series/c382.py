while True:
    try:
        a = input()
    except EOFError:
        break
    print(int(eval(a)))
