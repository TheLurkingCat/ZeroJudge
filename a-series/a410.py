s = [int(x) for x in input().split()]
delta = s[0] * s[4] - s[1] * s[3]
deltax = s[2] * s[4] - s[1] * s[5]
deltay = s[0] * s[5] - s[2] * s[3]
if delta:
    ans = 'x={:.2f}\ny={:.2f}'.format(deltax/delta, deltay/delta)
    print(ans)
elif not(delta or deltax or deltay):
    print("Too many")
else:
    print("No answer")
