output = []
while True:
    N, M = [int(x) for x in input().split()]
    if N:
        C = 1
        T = 1
        K = N // 2
        if K < M:
            M = N - M
        for i in range(M):
            C *= (N-i)
            T *= (i+1)
        C //= T
        output.append(str(C))
    else:
        break
print('\n'.join(output))