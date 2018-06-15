x = int(input())
for _ in range(x):
    origin = []
    after = []
    push_origin = origin.append
    push_after = after.append
    a, b = [int(x) for x in input().split()]
    for _ in range(a):
        t = input().split()
        push_origin(t)
        push_after(t[::-1])
    if origin == after[::-1]:
        print('go forward')
    else:
        print('keep defending')
