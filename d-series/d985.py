while True:
    try:
        a = int(input())
    except EOFError:
        break
    for i in range(1, a+1):
        best = 0
        avg = 0
        b = int(input())
        for _ in range(b):
            minute, second = [int(x) for x in input().split()]
            time = minute * 60 + second
            avg += time
            best = min(time, best) if best else time
        avg //= b
        best = divmod(best, 60)
        avg = divmod(avg, 60)
        print('Track {}:'.format(i))
        print('Best Lap: {} minute(s) {} second(s).'.format(best[0], best[1]))
        print('Average: {} minute(s) {} second(s).\n'.format(avg[0], avg[1]))
