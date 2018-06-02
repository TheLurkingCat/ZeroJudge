s = [int(x) for x in input().split()]
delta = s[0] * s[4] - s[1] * s[3]
deltax = s[2] * s[4] - s[1] * s[5]
deltay = s[0] * s[5] - s[2] * s[3]
if delta:
    ans = 'x={:.2f}\ny={:.2f}'.format(deltax/delta, deltay/delta)
    print(ans)
elif delta == 0 and deltax == 0 and deltay == 0:
    print("Too many")
else:
    print("No answer")
