ans = []
while True:
    try:
        s = s = [int(x) for x in input().split()]
    except EOFError:
        break
    tmp = s[0] % (2 ** s[1])
    if tmp:
        ans.append("可惡!!算了這麼久{}竟然無法被2的{}次整除".format(s[0], s[1]))
    else:
        ans.append("YA!!終於算出{}可被2的{}次整除了!!".format(s[0], s[1]))
print('\n'.join(ans))
