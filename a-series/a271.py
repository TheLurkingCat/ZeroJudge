a = int(input())
output = []
for _ in range(a):
    poison = 0
    a = {str(x+1): int(y) for x, y in enumerate(input().split())}
    a['0'], a['3'], a['4'] = 0, -a['3'], -a['4']
    b = input()
    weight = a['6']
    if not b:
        output.append('{}g'.format(weight))
        continue
    for food in b.split():
        weight -= poison
        if weight <= 0:
            output.append('bye~Rabbit')
            break
        if food == '4':
            poison += a['5']
        weight += a[food]
    else:
        if weight > 0:
            output.append('{}g'.format(weight))
        else:
            output.append('bye~Rabbit')
print('\n'.join(output))