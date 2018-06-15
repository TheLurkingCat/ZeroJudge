from queue import Queue
BFS_Queue = Queue()
visited = set()
STOP = False
n = int(input())
end = (n-2, n-2)
map = [input() for _ in range(n)]
empty = BFS_Queue.empty
next_step = BFS_Queue.get
add_state = BFS_Queue.put
visit = visited.add


def BFS(step, x, y):
    global STOP
    temp = (x, y)
    step += 1
    if temp in visited or not (-1 < x < n and -1 < y < n) or map[x][y] == '#':
        return
    if temp == end:
        print(step)
        exit()
    visit(temp)
    add_state((step, x, y+1))
    add_state((step, x+1, y))
    add_state((step, x-1, y))
    add_state((step, x, y-1))


add_state((0, 1, 1))
while True:
    if empty():
        print("No solution!")
        break
    BFS(*next_step())
