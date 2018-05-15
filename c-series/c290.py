a = [int(x) for x in input()]
odd = sum(a[::2])
even = sum(a[1::2])
ans = abs(odd - even)
print(ans)