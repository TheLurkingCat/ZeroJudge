while True:
    try:
        n = int(input())
    except EOFError:
        break
    s = [1]
    temp = 1
    for num in range(1, 50):
        s.append(s[num-1]+temp)
        temp += n
    ans = sum(s)
    print(ans)
