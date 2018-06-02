a = int(input())
output = []
cap = 1e-10
for i in range(a):
    before, after = [int(x) for x in input().split()]
    change = after / before * 100
    change -= 100
    state = 'keep' if -7 < change < 10 else 'dispose'
    change += cap if change > 0 else -cap
    change = round(change, 2)
    if not change:
        change = 0.00
    output.append('{:.2f}% {}'.format(change, state))
print('\n'.join(output))
