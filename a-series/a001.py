while True:
    try:
        print("hello,", input())
    except EOFError:
        break
