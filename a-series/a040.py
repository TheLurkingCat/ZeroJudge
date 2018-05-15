while True :
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = []
    for num in range(a, b+1):
        num = str(num)
        length = len(num)
        check = str(sum([pow(int(x), length) for x in list(num)]))
        if check == num: 
            ans.append(num)
    if ans:
        print(' '.join(ans))
    else:
        print("none")
