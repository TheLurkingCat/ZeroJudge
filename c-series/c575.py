def check(R):
    global N, K
    num = 0
    i = 0
    while i < N:
        num += 1
        s = sites[i] + R
        if num > K:
            return False
        if sites[N - 1] <= s:
            return True
        while (sites[i] <= s):
            i += 1


N, K = (int(x) for x in input().split())
sites = [int(x) for x in input().split()]
sites.sort()
R = sites[-1] - sites[0]
if K != 1:
    r = 1
    while check(R-1):
        rr = (r + R) // 2
        if check(rr):
            R = rr
        else:
            r = rr + 1
        if r == R:
            break
print(R)
