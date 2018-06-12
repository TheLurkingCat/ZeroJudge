a = int(input())
output = []
output_append = output.append
for _ in range(a):
    x, y = [int(x, 8) for x in input().split()]
    output_append(format(x+y, 'x').upper())
print(*output, sep='\n')
