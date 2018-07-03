from math import log10

ans = []
push = ans.append
while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    x = a - b if a / 2 < b else b
    target = 0
    for y in range(x):
        target += log10(a - y) - log10(x - y)
    push(int(target)+1)
print(*ans, sep='\n')
