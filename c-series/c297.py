from collections import deque
from itertools import zip_longest

now = 0
out = 0
base = deque([0, 0, 0], maxlen=4)
score = 0
temp = []
s = []

for x in range(9):
    a = input().split()
    del a[0]
    temp.append(a)

for x in zip_longest(*temp):
    s.extend(x)

target = int(input())

for state in s:
    if state == 'GO' or state == 'FO' or state == 'SO':
        now += 1
        if now == target:
            print(score)
        if out == 2:
            out = 0
            base = deque([0, 0, 0], maxlen=4)
        else:
            out += 1
    elif state == '1B':
        base.appendleft(1)
        if len(base) == 4 and base.pop():
            score += 1
    elif state == '2B':
        base.appendleft(1)
        if len(base) == 4 and base.pop():
            score += 1
        base.appendleft(0)
        if len(base) == 4 and base.pop():
            score += 1
    elif state == '3B':
        base.appendleft(1)
        if len(base) == 4 and base.pop():
            score += 1
        base.appendleft(0)
        if len(base) == 4 and base.pop():
            score += 1
        base.appendleft(0)
        if len(base) == 4 and base.pop():
            score += 1
    elif state == 'HR':
        score += sum(base) + 1
        base = deque([0, 0, 0], maxlen=4)
