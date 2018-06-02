from itertools import combinations
numbers = [int(x) for x in input().split()]
while numbers[0]:
    output = []
    n = numbers.pop(0)
    m = numbers.pop(-1)
    numbers.sort()
    answer = list(combinations(numbers, m))
    for ans in answer:
        output.append(' '.join(map(str, ans)))
    numbers = [int(x) for x in input().split()]
    print('\n'.join(output))
