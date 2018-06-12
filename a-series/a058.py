a = int(input())
s = [0, 0, 0]
for _ in range(a):
    i = int(input()) % 3
    s[i] += 1
print(*s)
