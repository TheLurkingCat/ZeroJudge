primes = {2, 7, 61, 97}
out = []
push = out.append
add = primes.add


def check(n, s, x):
    if x != 1 and x != n - 1:
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False
    return True


def isPrime(n):
    if n == 1:
        return False
    if n in primes:
        return True
    d = n - 1
    s = 0
    while not d % 2:
        d >>= 1
        s += 1
    return check(n, s, pow(2, d, n)) and check(n, s, pow(7, d, n)) and check(n, s, pow(61, d, n))


while True:
    try:
        n = int(input())
    except EOFError:
        break
    if isPrime(n):
        add(n)
        push("質數")
    else:
        push("非質數")
print(*out, sep='\n')
