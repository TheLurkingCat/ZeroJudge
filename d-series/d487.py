def chechun(x):
    if x == 0:
        return 1
    return x * chechun(x-1)
while True:
    try:
        i = int(input())
    except EOFError:
        break
    ans = ""
    x = i
    if i == 0:
        ans += "1 * "
    while x > 0:
        ans += str(x) + " * "
        x -= 1
    ans = ans[:len(ans)-2]
    print("{}! = {}= {}".format(i, ans, chechun(i)))
    
