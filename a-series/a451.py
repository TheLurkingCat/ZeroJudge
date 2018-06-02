def Fibonacci(max):
    n, a, b = 1, 0, 1
    if max == 0:
        return 0
    while n < max:
        a, b = b, a + b
        n = n + 1
    return b


while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = Fibonacci(s[0]) % pow(2, s[1])
    print(ans)
