while True:
    try:
        a = input()
    except EOFError:
        break
    ans = []
    s = {y: str(x+1) for x, y in enumerate(input().split())}
    c = (x for x in input().split())
    for num in c:
        try:
            ans.append(s[num])
        except KeyError:
            ans.append('0')
print('\n'.join(ans))
