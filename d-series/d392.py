out = []
push = out.append
while True:
    try:
        ans = sum([int(x) for x in input().split()])
    except EOFError:
        break
    push(ans)
print(*out, sep='\n')
