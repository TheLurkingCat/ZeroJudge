while True:
    try:
        i = int(input())
    except EOFError:
        break
    if i < 11:
        print(6 * i)
    elif i < 21:
        print(2 * i + 40)
    elif i < 41:
        print(i + 60)
    else:
        print("100")
