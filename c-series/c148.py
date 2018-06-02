a = int(input())
temp = ['*' * x for x in range(1, a+1)]
print(*temp, sep='\n')
