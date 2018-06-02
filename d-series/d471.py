from itertools import product
output = []
while True:
    try:
        a = int(input())
    except EOFError:
        break
    for ans in list(product('01', repeat=a)):
        output.append(''.join(map(str, ans)))
print('\n'.join(output))
