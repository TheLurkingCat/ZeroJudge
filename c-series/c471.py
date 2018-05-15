a = input()
ans = 0
k = []
w = [int(x) for x in input().split()]
add_all = sum(w)
s = [int(x) for x in input().split()]
for i, x in zip(w, s):
    try:
        k.append((x/i, i, x))
    except ZeroDivisionError:
        k.append((float('inf'), i, x))
k.sort()
for i in range(len(k)):
    add_all -= k[i][1]
    ans += add_all * k[i][2]
print(ans)