a, b = [int(x) for x in input().split()]
if a > b:
    a, b = b, a
if a & 1:
    a += 1
if b & 1:
    b -= 1
print(((b - a) // 2 + 1) * (a + b) // 2)
