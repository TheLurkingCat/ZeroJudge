z = int(input())
for n in range(1, z+1):
    output = 'Case {}: {}'
    s = sorted([int(x) for x in input().split()])
    k = len(set(s))
    if s[0] + s[1] <= s[2]:
        print(output.format(n, 'Invalid'))
    elif k == 1:
        print(output.format(n, 'Equilateral'))
    elif k == 2:
        print(output.format(n, 'Isosceles'))
    else:
        print(output.format(n, 'Scalene'))