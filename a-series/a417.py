t = int(input())
output = []
for _ in range(t):
    n, m = input().split()
    n = int(n)
    array = {x: {y: 0 for y in range(n)} for x in range(n)}
    x = 1
    for i in range((n+1)//2):
        k = n - 2 * i - 1
        for j in range(k):
            array[i][i+j] = x
            x += 1
        for j in range(k):
            array[i+j][n-i-1] = x
            x += 1
        for j in range(k):
            array[n-i-1][n-i-j-1] = x
            x += 1
        for j in range(k):
            array[n-i-j-1][i] = x
            x += 1
    if n & 1:
        array[n//2][n//2] = x
    for i in range(n):
        temp = []
        for j in range(n):
            if m == '1':
                temp.append('%5d' % array[i][j])
            else:
                temp.append('%5d' % array[j][i])
        output.append(''.join(temp))
    output.append('')
print('\n'.join(output))
