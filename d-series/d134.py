while True:
    N, M = [int(x) for x in input().split()]
    C = 1
    t = 1
    if N:
        for i in range(M):
            C *= (N-i)
            t *= (i+1)
        C //= t
        print('{} things taken {} at a time is {} exactly.'.format(N, M, C))
    else:
        break
