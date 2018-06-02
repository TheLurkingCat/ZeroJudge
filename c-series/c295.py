N, M = [int(x) for x in input().split()]
temp = []
output = []
for _ in range(N):
    temp.append(max([int(x) for x in input().split()]))
S = sum(temp)
print(S)
for i in temp:
    if S % i == 0:
        output.append(str(i))
if output:
    print(' '.join(output))
else:
    print(-1)
