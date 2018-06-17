a = int(input())
for _ in range(a):
    yee = 100 - sum([int(x) for x in input().split()])
    if yee <= 0 or yee >= 100:
        print('evil!!')
    else:
        if yee <= 60:
            if yee <= 30:
                print('sad!')
            else:
                print('hmm~~')
        else:
            print('Happyyummy')
