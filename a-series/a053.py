while True:
    try:
        i = int(input())
    except EOFError:
        break
    if i < 41:
        if i < 21:
            if i < 11:
                print(6 * i)
            else:
                print(2 * i + 40)
        else:
            print(i + 60)
    else:
        print("100")
