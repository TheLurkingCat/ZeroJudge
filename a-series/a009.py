while True:
    try:
        a = input()
    except EOFError:
        break
    s = []
    for char in a:
        s.append(chr(ord(char) - 7))
    print(''.join(s))
