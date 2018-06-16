ans = 0
for _ in range(5):
    a, b, c = sorted([int(x) for x in input().split()])
    if a + b > c:
        ans += 1
print(ans)
