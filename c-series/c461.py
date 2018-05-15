a, b, c = [bool(int(x)) for x in input().split()]
output = []
if a & b == c:
    output.append('AND')
if a | b == c:
    output.append('OR')
if a ^ b == c:
    output.append('XOR')
if output:
    print(*output, sep='\n')
else:
    print('IMPOSSIBLE')