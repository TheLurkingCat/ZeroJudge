while True:
    try:
        a = ord(input()[:1])
    except EOFError:
        break
    b = ord(input()[:1])
    print((b-a+26) % 26)
