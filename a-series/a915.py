from operator import itemgetter
output = []
a = int(input())
s = []
for i in range(a):
    x, y = [int(x) for x in input().split()]
    s.append((x, y))
s.sort(key=itemgetter(0, 1))
for item in s:
    output.append('{} {}'.format(item[0], item[1]))
print('\n'.join(output))
