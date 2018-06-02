while True:
    try:
        s = input()
    except EOFError:
        break
    print("yes" if s == s[::-1] else 'no')
