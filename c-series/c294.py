a, b, c = sorted([int(x) for x in input().split()])
left = a * a + b * b
right = c * c
print(a, b, c)
if a+b > c:
    if left > right:
        print('Acute')
    elif left == right:
        print('Right')
    else:
        print('Obtuse')
else:
    print('No')