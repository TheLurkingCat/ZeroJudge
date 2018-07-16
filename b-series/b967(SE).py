max_depth = 0


def DFS(node):
    global max_depth
    k = len(Tree[node])
    if k == 0:
        return 0
    if k == 1:
        return DFS(Tree[node][0]) + 1
    else:
        for i in range(k):
            result = DFS(Tree[node][i]) + 1
            if i == 0:
                max_1 = result
            elif i == 1:
                if max_1 >= result:
                    max_2 = result
                else:
                    max_1, max_2 = result, max_1
            else:
                if max_1 <= result:
                    max_2, max_1 = max_1, result
                elif max_2 < result:
                    max_2 = result
        max_depth = max(max_depth, max_1 + max_2)
        return max_1


output = []
push = output.append
while True:
    max_depth = 0
    try:
        n = int(input())
    except EOFError:
        break
    is_child = [False] * n
    Tree = [[] for _ in range(n)]
    for i in range(1, n):
        a, b = (int(x) for x in input().split())
        Tree[a].append(b)
        is_child[b] = True
    root = is_child.index(False)
    max_distance = DFS(root)
    push(max(max_distance, max_depth))
print(*output, sep='\n')
