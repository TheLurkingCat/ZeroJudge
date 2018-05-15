a = int(input())
b = int(input())
temp = []
num = 0
for _ in range(b):
    x, y = input().split()
    y = int(y, int(x))
    state = True if y < a else False
    y += a
    s = format(y, 'b').count('1')
    temp.append((s, state))
temp.sort(reverse=True)
max_s = temp[0][0]
for s, state in temp:
    if s == max_s and state:
        num += 1
print(max_s, num)