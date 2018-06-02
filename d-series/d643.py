from math import ceil, sqrt
a = input()
check = a
length = len(a)
t = ''.join(sorted(a))
output = []
if t != a:
    output.append(t)
a = list(a)
factors = []
for i in range(2, ceil(sqrt(length))+1):
    k = length / i
    if k.is_integer():
        factors.append((i, int(k)))
        factors.append((int(k), i))
factors.sort()
for i, k in factors:
    temp = []
    for x in range(k):
        temp.append(''.join(a[x*i:(x+1)*i]))
    temp.sort()
    t = ''.join(temp)
    if not (t in output or t == check):
        output.append(t)
if output:
    print('\n'.join(output))
else:
    print('bomb!')
