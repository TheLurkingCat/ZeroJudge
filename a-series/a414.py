a = int(input())
while a:
    a = bin(a)[2:]
    a = a[::-1]
    ans = 0
    for num in a:
        if num == '0':
            break
        ans+=1
    print(ans)
    a = int(input())