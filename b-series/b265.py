from collections import Counter
a = int(input())
while a:
    temp = []
    for _ in range(a):
        temp.append(''.join(sorted(input().split())))
    c = Counter(temp).most_common()
    ans = c[0][1]
    for x in range(len(c)-1):
        if c[x][1] == c[x+1][1]:
            ans += c[x][1]
        else:
            break
    print(ans)
    a = int(input())