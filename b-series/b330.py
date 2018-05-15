n, x = input().split()
s = [str(x) for x in range(1, int(n)+1)]
temp = ''.join(s)
print(temp.count(x))