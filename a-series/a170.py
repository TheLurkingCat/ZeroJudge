a = int(input())
output = []
for _ in range(a):
    x, y = [int(x, 8) for x in input().split()]
    output.append(format(x+y, 'x').upper())
print(*output, sep='\n')