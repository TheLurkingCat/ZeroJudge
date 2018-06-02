def paint(x, y):
    global a
    global pic
    if not (0 <= x < a and 0 <= y < a):
        return
    if pic[x][y] == '+':
        return
    pic[x][y] = '+'
    paint(x+1, y)
    paint(x-1, y)
    paint(x, y+1)
    paint(x, y-1)


output = []
a = int(input())
pic = []
for i in range(a):
    pic.append(list(input()))
pos_x, pos_y = [int(x) for x in input().split()]
paint(pos_x, pos_y)
for lines in pic:
    output.append(''.join(lines))
print('\n'.join(output))
