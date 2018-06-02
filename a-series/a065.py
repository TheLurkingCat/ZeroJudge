while True:
    try:
        a = input()
    except EOFError:
        break
    ans = [str(abs(ord(a[x]) - ord(a[x+1]))) for x in range(6)]
    print(''.join(ans))
