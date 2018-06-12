while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = []
    ans_append = ans.append
    for num in range(a, b+1):
        num = str(num)
        length = len(num)
        check = str(sum([pow(int(x), length) for x in num]))
        if check == num:
            ans_append(num)
    if ans:
        print(*ans)
    else:
        print("none")
