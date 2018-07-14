N, M, K = [int(x) for x in input().split()]
arr = list(range(1, N + 1))
now = 0
while K:
    now += M - 1
    now %= N
    K -= 1
    N -= 1
    del arr[now]
now %= N
print(arr[now])
