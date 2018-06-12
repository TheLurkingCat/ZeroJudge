output = []
output_append = output.append
out = []
out_append = out.append
make = ''.join


def DFS(left, right, k):
    c = 2 * n
    if k == c:
        out_append(make(output))
        return
    if left < n:
        output_append('(')
        DFS(left+1, right, k+1)
        del output[-1]
    if left > right:
        output_append(')')
        DFS(left, right+1, k+1)
        del output[-1]


while True:
    try:
        n = int(input())
    except Exception:
        print(*out, sep='\n')
        break
    DFS(0, 0, 0)
    out_append('')
