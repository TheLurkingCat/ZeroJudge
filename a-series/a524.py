from itertools import permutations
output = []
while True:
    try:
        a = int(input())
    except ValueError:
        break
    numbers = list(range(1, a+1))
    for ans in list(permutations(numbers, a))[::-1]:
        output.append(''.join(map(str, ans)))
print('\n'.join(output))
