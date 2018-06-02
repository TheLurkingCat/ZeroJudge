a = int(input())
for _ in range(a):
    x = input()
    x = x.replace('/', '//')
    print(eval(x))
