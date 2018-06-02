N, K, W = [int(x) for x in input().split()]
cache = N
while cache > K:
    cache, left = divmod(cache, K)
    N += cache * W
    cache += cache * W + left
print(N)
