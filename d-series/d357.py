from itertools import combinations
def check (n, s, x):
    if x != 1 and x != n - 1:
        for r in range(1, s):
            x = pow(x, 2 ,n)
            if x == n - 1:
                return 1
        return 0
    return 1

def isPrime (n):
    primes = (2, 7, 61, 97)
    if n == 1:
        return 0
    if n in primes:
        return 1
    d = n - 1
    s = 0
    while not d % 2:
        d //= 2
        s += 1
    return check(n, s, pow(2, d, n)) and check(n, s, pow(7, d, n)) and check(n, s, pow(61, d, n))

ans = 0
n, k = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
for t in list(combinations(s, k)):
    temp = sum(t)
    if isPrime(temp):
        ans += 1
print(ans)