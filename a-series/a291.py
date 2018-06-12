answer = []
ans_append = answer.append
while True:
    try:
        correct = input().split()
    except EOFError:
        break
    num = int(input())
    for _ in range(num):
        ans = correct.copy()
        rmv = ans.remove
        case = input().split()
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
        for i in case:
            if i in ans:
                B += 1
                rmv(i)
        ans_append('{}A{}B'.format(A, B))
print(*answer, sep='\n')
