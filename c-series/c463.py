from collections import deque

Tree = deque()
total_nodes = int(input())
parent = [0] * (total_nodes+1)
depth = [-1] * (total_nodes+1)
num = [0] * (total_nodes+1)
for i in range(1, total_nodes + 1):
    n_nodes, *childs = [int(x) for x in input().split()]
    if n_nodes:
        num[i] = n_nodes
        for child in childs:
            parent[child] = i
    else:
        Tree.append(i)
        depth[i] = 0
while Tree:
    root = Tree.popleft()
    depth[parent[root]] = max(depth[parent[root]], depth[root] + 1)
    num[parent[root]] -= 1
    if num[parent[root]] == 0:
        Tree.append(parent[root])
print(root)
print(sum(depth[1:]))
