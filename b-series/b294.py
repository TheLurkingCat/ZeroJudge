a = input()
s = [int(x) for x in input().split()]
ans = 0
for date, num in enumerate(s):
    ans += num * (date+1)
print(ans)
