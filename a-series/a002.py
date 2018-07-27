while True:
    try:
        print(sum(int(x) for x in input().split()))
    except EOFError:
        break
