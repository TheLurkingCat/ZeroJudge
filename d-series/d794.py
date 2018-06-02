from bisect import bisect
a = [-1]
k = int(input())
output = []
for _ in range(k):
    c = int(input())
    z = bisect(a, c)
    output.append(z)
    a.insert(z, c)
f = map(str, output)
print('\n'.join(f))
