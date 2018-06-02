output = []
while True:
    try:
        n, m = [int(x) for x in input(). split()]
    except EOFError:
        break
    table = {int(x): {} for x in range(n+1)}
    for i in range(n+1):
        if i:
            s = [int(x) for x in input(). split()]
        for j in range(n+1):
            if i and j:
                table[i][j] = s[j-1] + table[i-1][j] + \
                    table[i][j-1] - table[i-1][j-1]
            else:
                table[i][j] = 0
    for i in range(m):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        output.append(str(table[x2][y2] - table[x1-1]
                          [y2] - table[x2][y1-1] + table[x1-1][y1-1]))
print('\n'.join(output))
