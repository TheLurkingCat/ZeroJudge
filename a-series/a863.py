while True:
    try:
        a = input()
    except EOFError:
        break
    ans = a
    a = int(a)
    s = []
    k = 0
    while a != 1:
        k += 1
        if k == 100:
            break
        temp = 0
        for num in str(a):
            temp += int(num) ** 2
        a = temp
    else:
        print(ans + " is a happy number")
        continue
    print(ans + " is an unhappy number")
