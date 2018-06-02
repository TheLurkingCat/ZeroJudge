a = int(input())
while a:
    for i in range(1, a+1):
        print('_' * (a-i) + '+' * i)
    a = int(input())
