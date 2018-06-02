while True:
    try:
        b, n = input().split()
    except EOFError:
        break
    b = int(b)
    number_before = 0
    number_after = 0
    length = len(n) - 1
    for i, num in enumerate(n):
        number_after += pow(int(num), length+1)
        number_before += pow(b, length-i) * int(num)
    if number_after == number_before:
        print('YES')
    else:
        print('NO')
