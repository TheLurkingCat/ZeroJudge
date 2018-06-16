from calendar import isleap
ans = 0
a, b = [int(x) for x in input().split()]
for x in range(a, b + 1):
    if isleap(x):
        ans += 1
print(ans)
