a = int(input())
while a:
    s = [int(x) for x in input().split()]
    ans = []
    for num in s:
        ans.append(str(num))
    if s[1] - s[0] == s[2] - s[1] and s[3] - s[2] == s[2] - s[1]:
        ans.append(str(2 * s[3] - s[2]))
    else:
        ans.append(str((s[3] ** 2) // s[2]))
    print (' '.join(ans))
    a -= 1