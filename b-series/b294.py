a = input()
s = [int(x) for x in input().split()]
ans = 0
for date, num in enumerate(s, 1):
    ans += num * date
print(ans)
