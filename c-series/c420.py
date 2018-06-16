n = int(input())
c = 2 * n - 1
for i in range(1, 2 * n, 2):
    k = '*' * i
    print(k.center(c, '_'))
