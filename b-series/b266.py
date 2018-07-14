def rotate(x, column, row):
    temp = [[0] * row for x in range(column)]
    for i in range(row):
        for j in range(column):
            temp[column-j-1][i] = x[i][j]
    return (temp, row, column)


def flip(x):
    return x[::-1]


matrix = []
R, C, M = (int(x) for x in input().split())
for _ in range(R):
    matrix.append([int(x) for x in input().split()])
acts = [int(x) for x in input().split()][::-1]
for action in acts:
    if action:
        matrix = flip(matrix)
    else:
        matrix, C, R = rotate(matrix, C, R)
print(R, C)
for row in matrix:
    print(*row)
