x = dict()
y = dict()
ans = 0
for a in input().split():
    c, d = a.split(':')
    x[c] = int(d)
for a in input().split():
    c, d = a.split(':')
    y[c] = int(d)
for a in x.keys() & y.keys():
    ans += x[a] * y[a]
print(ans)
