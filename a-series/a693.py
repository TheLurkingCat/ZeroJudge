while True:
    try:
        s1 = [int(x) for x in input().split()]
    except EOFError:
        break
    s2 = [0]
    for i, x in enumerate(input().split()):
        s2.append(int(x)+s2[i])
    ans = []
    for _ in range(s1[1]):
        s3 = [int(x) for x in input().split()]
        left = s3[0] - 1
        right = s3[1]
        temp = s2[right] - s2[left]
        ans.append(str(temp))
    print('\n'.join(ans))