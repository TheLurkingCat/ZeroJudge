from operator import itemgetter
while True:
    try:
        a = input()
    except EOFError:
        break
    # 個位數，十位數分開來存，個位數大小反轉(0=9,1=8...)
    s = sorted([(int(x), 9-int(x) % 10)
                for x in input().split()], key=itemgetter(1, 0), reverse=True)
    # 列表是tuple，只取原數字
    ans = next(zip(*s))
    print(*ans)
