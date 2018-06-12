a = int(input())
output = []
output_append = output.append
while a:
    a = format(a, 'b').split('0')
    output_append(len(a[-1]))
    a = int(input())
print(*output, sep='\n')
