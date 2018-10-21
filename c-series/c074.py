from itertools import combinations

a = input().split()
while True:
    del a[0]
    for ans in combinations(a, 6):
        print(*ans)
    a = input().split()
    if (a == ['0']):
        break
    print()
