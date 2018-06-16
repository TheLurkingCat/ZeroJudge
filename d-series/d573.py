out = []
push_out = out.append
while True:
    sheet = []
    push = sheet.append
    try:
        a = int(input())
    except EOFError:
        break
    for _ in range(a):
        s = input().split()
        del s[0]
        del s[0]
        push(set(s))
    k = input()
    for i, x in enumerate(sheet, 1):
        if k in x:
            push_out(i)
            break
print(*out, sep='\n')
