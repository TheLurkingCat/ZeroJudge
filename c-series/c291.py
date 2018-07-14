N = int(input())
number = [int(x) for x in input().split()]
state = [True] * N
ans = 0
Flag = True
for i in range(N):
    while state[i]:
        state[i] = False
        i = number[i]
        if Flag:
            ans += 1
            Flag = False
    Flag = True
print(ans)
