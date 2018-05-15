def f(n):
    if n < 5:
        return 0
    n //= 5
    return n + f(n)
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(f(n))