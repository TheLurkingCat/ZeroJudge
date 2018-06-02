L, R = [int(x) for x in input().split()]
s = [str(i) for i in range(L, R+1)]
string = ''.join(s)
ans = string.count('2')
print(ans)
