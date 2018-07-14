output = []
matrix = []
push = matrix.append
a = int(input())
pos = int(input())
for _ in range(a):
    push([int(x) for x in input().split()])
push = output.append
mid = a // 2
step = 1
x = y = mid
push(matrix[mid][mid])
Flag = True
while Flag:
    pos %= 4
    if pos == 0:
        for i in range(int(step)):
            y -= 1
            if y < 0:
                Flag = False
                break
            push(matrix[x][y])
        step += 0.5
    elif pos == 1:
        for i in range(int(step)):
            x -= 1
            if x < 0:
                Flag = False
                break
            push(matrix[x][y])
        step += 0.5
    elif pos == 2:
        for i in range(int(step)):
            y += 1
            try:
                push(matrix[x][y])
            except IndexError:
                Flag = False
                break
        step += 0.5
    else:
        for i in range(int(step)):
            x += 1
            try:
                push(matrix[x][y])
            except IndexError:
                Flag = False
                break
        step += 0.5
    pos += 1
print(*output, sep='')
