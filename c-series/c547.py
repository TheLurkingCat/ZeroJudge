a = [0, 1, 2]
push = a.append
for i in range(3, 10000):
    push((a[i-1] + a[i-2]) % 1000000007)
while True:
    try:
        c = int(input())
    except EOFError:
        break
    print(a[c])
