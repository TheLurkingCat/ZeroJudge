a = int(input())
ans = []
for _ in range(a):
    s = [int(x) for x in input().split()]
    if s[0] > s[1]:
        ans.append(">")
    elif s[1] > s[0]:
        ans.append("<")
    else:
        ans.append("=")
print('\n'.join(ans))
