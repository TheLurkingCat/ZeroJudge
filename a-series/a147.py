a = 1
while a:
    a = int(input())
    s = [i for i in range(a) if i % 7]
    print(*s)
