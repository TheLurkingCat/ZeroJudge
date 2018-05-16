while True:
    try:
        a = int(input())
    except EOFError:
        break
    b = input()
    c = int(input())
    if b == '/':
        print(a // c)
    else:
        print(a * c)