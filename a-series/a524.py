from itertools import permutations
from collections import deque
while True:
    output = deque()
    left = output.appendleft
    try:
        a = int(input())
    except Exception:
        break
    for ans in permutations(range(1, a+1), a):
        left(''.join(map(str, ans)))
    print(*output, sep='\n')
