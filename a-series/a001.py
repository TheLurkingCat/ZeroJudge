while True:
    try:
        a = input()
    except EOFError:
        break
    print("hello,", a)