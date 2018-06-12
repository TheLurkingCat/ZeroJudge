"""
TLE
"""
output = []
output_append = output.append


def Fibonacci(max):
    n, a, b = 1, 0, 1
    if max == 0:
        return 0
    while n < max:
        a, b = b, a + b
        n += 1
    return b


while True:
    try:
        n, m = [int(x) for x in input().split()]
    except EOFError:
        break
    if m > 1:
        output_append(Fibonacci(n) % (2 << (m - 1)))
    elif m:
        output_append(int(bool(m % 3)))
    else:
        output_append(Fibonacci(n))
print(*output, sep='\n')
