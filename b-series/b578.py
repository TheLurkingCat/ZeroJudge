a = int(input())
for _ in range(a):
    a, b, c = sorted([int(x)**2 for x in input().split()])
    t = a + b
    if t > c:
        print('acute triangle')
    elif t == c:
        print('right triangle')
    else:
        print('obtuse triangle')
