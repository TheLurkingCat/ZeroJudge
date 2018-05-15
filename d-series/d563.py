"""
b = [int(x) for x in input().split()]
del b[0]
prefix = 0
suffix = 0
ans = 0
for n in range(len(b)):
    prefix += b[n]
    suffix += b[-n-1]
    if prefix == suffix:
        ans += 1
print(ans)
"""
a = input()
print(20156 if a.startswith('1') else 1)