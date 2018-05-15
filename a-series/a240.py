m = int(input())
s = [0,5,8,8,2,3,5,2,9,4,1,1,7,6,4,7]
for _ in range(m):
    i = int(input())
    ans = 0
    for x in range(i):
        ans+=s[x%16]
    print (s[(i%16)-1],ans)