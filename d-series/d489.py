s = [int(x) for x in input().split()]
S = sum(s) / 2
ans = S * (S - s[0]) * (S - s[1]) * (S - s[2])
print(int(ans))