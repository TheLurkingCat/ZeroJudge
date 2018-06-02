from itertools import combinations
a = input().split()
while a != ['0']:
    del a[0]
    for ans in combinations(a, 6):
        print(*ans)
    print()
    a = input().split()
