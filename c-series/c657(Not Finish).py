from collections import OrderedDict
from operator import itemgetter

# 最早出現是指測資點還是測資
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
    print(*max(seq.items(), key=itemgetter(1)))
