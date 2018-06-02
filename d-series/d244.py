a = {}
for num in input().split():
    try:
        a[num] += 1
    except KeyError:
        a[num] = 0
for key, value in a.items():
    if value % 3:
        print(key)
        break
