x = int(input())
a = 1
b = 1
c = 1
x -= 3 
for i in range(x):
    a, b, c = b, c, a + b + c
print(c % 10007)