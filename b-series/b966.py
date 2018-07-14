from operator import itemgetter

output = []
push = output.append

while True:
    lines = []
    add = lines.append
    try:
        a = int(input())
    except EOFError:
        break
    for _ in range(a):
        add([int(x) for x in input().split()])
    lines.sort(key=itemgetter(0))
    now = 0
    ans = 0
    for x, y in lines:
        if y > now:
            ans += y - max(now, x)
            now = y
    push(ans)
print(*output, sep='\n')
