a = int(input())
for times in range(0, a):
    b = int(input())
    c = int(input())
    ans = 0
    for x in range(b, c+1):
        s = x ** 0.5
        if s.is_integer():
            ans += x
    print('Case {}: {}'.format(times+1, int(ans)))
