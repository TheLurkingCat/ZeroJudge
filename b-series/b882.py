h, m, s = [int(x) for x in input().split()]
x, s = divmod(s, 60)
x, m = divmod(x+m, 60)
h = (h+x) % 24
ans = '{:02}:{:02}:{:02}'.format(h, m, s)
print(ans)
