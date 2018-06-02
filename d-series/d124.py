while True:
    try:
        a = int(input())
    except EOFError:
        break
    print('no') if a % 3 else print('yes')
