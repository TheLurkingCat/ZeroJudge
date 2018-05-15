a = input()
s = [int(x) for x in input().split()]
buff = 0
load = False
for num in s:
    if num - buff < 0:
        load = True
    if num - buff >= 30:
        print(buff+30)
        break
    else:
        if load:
            buff += 5
            load = False
        else:
            buff = num + 5
else:
    print(buff+30)
