answer = []
while True:
    try:
        correct = [x for x in input().split()]
    except EOFError:
        break
    num = int(input())
    for _ in range(num):
        ans = correct.copy()
        case = [x for x in input().split()]
        A = 0
        i = 0
        while i < len(ans):
            if ans[i] == case[i]:
                del ans[i]
                del case[i]
                A += 1
            else:
                i += 1
        B = 0
        length = len(ans)
        for i in case:
            if i in ans:
                B += 1
                ans.remove(i)
        answer.append('{}A{}B'.format(A, B))
print('\n'.join(answer))