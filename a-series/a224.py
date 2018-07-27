from collections import Counter
from re import sub

while True:
    try:
        s = sub('[^a-z]', '', input().lower())
    except EOFError:
        break

    length = len(s)
    s = Counter(s)
    wrong = -1 if length & 1 else 0

    for x in s.most_common():
        if x[1] & 1:
            wrong += 1
            if wrong > 0:
                print('no...')
                break
    else:
        print('yes !')
