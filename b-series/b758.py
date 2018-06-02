s = [int(x) for x in input().split()]
s[1] += 30
ans = ""
s[0] += 2
if s[1] >= 60:
    s[1] -= 60
    s[0] += 1
if s[0] >= 24:
    s[0] -= 24
if s[0] < 10:
    ans += "0" + str(s[0])
else:
    ans += str(s[0])
ans += ":"
if s[1] < 10:
    ans += "0" + str(s[1])
else:
    ans += str(s[1])
print(ans)
