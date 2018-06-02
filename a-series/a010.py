def count_pow(x, y):
    result = 0
    while not x % y:
        x /= y
        result += 1
    return result


while True:
    try:
        i = int(input())
    except EOFError:
        break
    ans = ""
    a = 2
    while i > 1:
        if i % a == 0 and count_pow(i, a) != 1:
            temp = count_pow(i, a)
            i /= (a ** temp)
            ans += str(a) + "^" + str(temp)
        elif count_pow(i, a) == 1:
            ans += str(a)
            i /= a
        else:
            a += 1
            continue
        a += 1
        ans += " * "
    print(ans[: -3])
