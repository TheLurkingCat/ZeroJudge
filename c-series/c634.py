from operator import itemgetter
out = []
push = out.append
make_str = ''.join
primes = []


def p(n):
    t = 0
    for i in range(2, n+1):
        if not n % i:
            t += i
    return t


while True:
    x = []
    y = []
    push_x = x.append
    push_y = y.append
    try:
        a = input()
    except EOFError:
        break
    for num in a:
        if num.isdigit():
            push_x(num)
        else:
            push_y(num)
    N = int(make_str(x))
    try:
        T = 1 / p(N)
    except ZeroDivisionError:
        T = float('inf')
    try:
        N = 1 / N
    except ZeroDivisionError:
        N = float('inf')
    S = make_str(y)
    push((T, S, N, a))
out.sort(key=itemgetter(0, 1, 2))
print(*list(zip(*out))[3], sep='\n')
