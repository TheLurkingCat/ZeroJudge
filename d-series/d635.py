while True:
    a = int(input())
    if a < 0:
        print(-1)
        break
    print(format(a, 'o'))