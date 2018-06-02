from math import sqrt, ceil
print('PERFECTION OUTPUT')
while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    for a in s:
        ans = 1
        for i in range(2, a):
            if not a % i:
                ans += i
        if a == 1:
            ans = 0
        elif a == 0:
            break
        if ans > a:
            print("%5d  ABUNDANT" % a)
        elif ans == a:
            print("%5d  PERFECT" % a)
        else:
            print("%5d  DEFICIENT" % a)
print('END OF OUTPUT')
