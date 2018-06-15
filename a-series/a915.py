from operator import itemgetter
output = []
a = int(input())
s = [tuple([int(x) for x in input().split()]) for _ in range(a)]
s.sort(key=itemgetter(0, 1))
for item in s:
    output.append('{} {}'.format(*item))
print(*output, sep='\n')
