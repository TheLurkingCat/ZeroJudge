from collections import Counter
a = int(input())
b = int(input())
temp = Counter()
for _ in range(b):
    x, y = input().split()
    y = int(y, int(x))
    if y < a:
        y += a
        s = format(y, 'b').count('1')
        temp[s] += 1
k = sorted(temp.items(), reverse=True)
print(*k[0])
