from collections import Counter
from operator import itemgetter
while True:
    output = []
    try:
        a = input()
    except EOFError:
        break
    s = sorted(Counter([int(x) for x in input().split()]
                       ).most_common(), key=itemgetter(1, 0))
    k = s[-1][1]
    for x in s:
        if k == x[1]:
            output.append('{} {}'.format(*x))
    print('\n'.join(output))
