from collections import OrderedDict
n = int(input())
zoo = OrderedDict()
order = []
for _ in range(n):
    name, number, loc = input().split()
    if not name in order:
        order.append(name)
    number = int(number)
    try:
        temp = zoo[loc]
    except KeyError:
        zoo[loc] = dict()
        temp = zoo[loc]
    try:
        temp[name] += number
    except KeyError:
        temp[name] = number
for x in zoo.keys():
    outputstr = '{} : {}'
    temp = []
    for y in order:
        try:
            temp.append('{} {}'.format(y, zoo[x][y]))
        except KeyError:
            pass
    print(outputstr.format(x, ', '.join(temp)))