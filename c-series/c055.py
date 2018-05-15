while True:
    try:
        a = int(input())
    except EOFError:
        break
    ans = 1
    for i in range(1, a+1):
        ans *= i
    ans = str(ans).replace('0', '')
    print('{} -> {}'.format(a, ans[-1]))