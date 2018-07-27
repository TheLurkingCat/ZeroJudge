def count_pow(x, y):
    origin = x
    result = 0
    while not x % y:
        x //= y
        result += 1
    return result, origin // x


out = []
push_out = out.append

while True:
    try:
        i = int(input())
    except EOFError:
        break
    ans = []
    push = ans.append
    a = 2
    while i > 1:
        temp, t = count_pow(i, a)
        if not i % a and temp != 1:
            i //= t
            push("{}^{}".format(a, temp))
        elif temp == 1:
            push(str(a))
            i //= a
        a += 1
    push_out(' * '.join(ans))
print(*out, sep='\n')
