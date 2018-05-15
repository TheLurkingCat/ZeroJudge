while True:
    try:
        a = int(input())
    except EOFError:
        break
    s = input().split()
    for x in range(a):
        print(*s)
        s = s[::-1]
        s.pop()