a = input()
lenth = len(a)
lenth2 = lenth
times = 0
a = str(a) * 2
while lenth > 0:
    print(a[times: times+lenth2])
    times += 1
    lenth -= 1
