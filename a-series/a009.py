while True:
    try:
        a = [chr(ord(char) - 7) for char in input()]
    except EOFError:
        break
    print(*a, sep='')
