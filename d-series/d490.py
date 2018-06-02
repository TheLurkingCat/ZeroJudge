a, b = [int(x) for x in input().split()]
if a & 1:
    a += 1
if b & 1:
    b -= 1
n = (b - a + 2) // 2
ans = (a + b) * n // 2
print(ans)
