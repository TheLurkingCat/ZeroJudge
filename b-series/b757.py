a = float(input())
ans = a * 9 / 5 + 32
if ans.is_integer():
    print(str(ans)[:-2])
else:
    print(ans)
