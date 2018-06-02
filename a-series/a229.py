output = []


def DFS(left, right, k):
    c = 2 * n
    if k == c:
        print(''.join(output))
        return
    if left < n:
        output.append('(')
        DFS(left+1, right, k+1)
        del output[-1]
    if left > right:
        output.append(')')
        DFS(left, right+1, k+1)
        del output[-1]


while True:
    try:
        n = int(input())
    except ValueError:
        break
    DFS(0, 0, 0)
