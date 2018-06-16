"""
Answer:29786 + 850 + 850 = 31486
"""
from itertools import permutations
x = 'FORTY'
y = 'TEN'
z = 'SIXTY'
for k in permutations('0123456789'):
    c = str.maketrans('EFINORSTXY', ''.join(k))
    t1 = x.translate(c)
    t2 = y.translate(c)
    t3 = z.translate(c)
    if int(t1) + int(t2) * 2 == int(t3):
        print('{0} + {1} + {1} = {2}'.format(t1, t2, t3))
