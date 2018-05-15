a = 1
while a:
    a = int(input())
    s = [str(i) for i in range(a) if i % 7]
    print (' '.join(s))