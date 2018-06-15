ans = []
push = ans.append
while True:
    try:
        s1 = [int(x) for x in input().split()]
    except EOFError:
        break
    s2 = {0: 0}
    for i, x in enumerate(input().split()):
        s2[i+1] = int(x) + s2[i]
    for _ in range(s1[1]):
        left, right = [int(x) for x in input().split()]
        left -= 1
        push(s2[right] - s2[left])
print(*ans, sep='\n')
