a = int(input())
stack = []
for _ in range(a):
    x = input().split()
    if len(x) > 1:
        stack.append(x[1])
    elif x[0] == '1':
        stack.pop()
    else:
        print(stack[-1])