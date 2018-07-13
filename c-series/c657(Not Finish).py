from collections import OrderedDict
from operator import itemgetter

while True:
    seq = OrderedDict()
    try:
        x = input() + '!'
    except EOFError:
        break
    t = x[0]
    count = 0
    for word in x:
        if t == word:
            count += 1
        else:
            seq[t] = max(seq[t], count) if t in seq else count
            count = 1
            t = word
    M = 0
    word = ''
    for x, y in seq.items():
        if y > M:
            M = y
            word = x
    print(word, M)
