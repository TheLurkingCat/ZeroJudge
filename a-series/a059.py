from math import sqrt
a = int(input())
for times in range(a):
    b = int(input())
    c = int(input())
    ans = 0
    for x in range(b, c+1):
        s = sqrt(x)
        if s.is_integer():
            ans += x
    print('Case {}: {}'.format(times+1, ans))
