def vaild(x, y, step):
    if maze[x][y] == '.':
        return True
    if maze[x][y] == '#' or maze[x][y] <= step:
        return False
    return True

a = int(input())
maze = []
stack = [(1, 1)]
limit = a ** 2
for _ in range(a):
    maze.append(list(input()))
maze[1][1] = 1
for step in range(2, limit):
    if stack:
        for i in range(len(stack)):
            x, y = stack.pop(0)
            if vaild(x+1, y, step):
                maze[x+1][y] = step
                stack.append((x+1, y))
            if vaild(x-1, y, step):
                maze[x-1][y] = step
                stack.append((x-1, y))
            if vaild(x, y+1, step):
                maze[x][y+1] = step
                stack.append((x, y+1))
            if vaild(x, y-1, step):
                maze[x][y-1] = step
                stack.append((x, y-1))
    else:
        print('No solution!')
        break
    if (a-2, a-2) in stack:
        print(step)
        break