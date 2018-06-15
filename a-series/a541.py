output = []
push = output.append
x = int(input())
dictionary = set()
memorize = dictionary.add
for _ in range(x):
    memorize(input())
x = int(input())
for _ in range(x):
    c = input()
    if c in dictionary:
        push('yes')
    else:
        push('no')
        memorize(c)
print(*output, sep='\n')
