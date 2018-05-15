a = input()
while not a == "0":
    s = [int(x) for x in input().split()]
    ans = [str(x) for x in sorted(s)]
    print(' '.join(ans))
    a = input()
    