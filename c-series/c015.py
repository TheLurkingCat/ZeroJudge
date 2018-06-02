a = int(input())
for _ in range(a):
    x = input()
    y = x[::-1]
    counter = 0
    while x != y or not counter:
        x = str(int(x) + int(y))
        y = x[::-1]
        counter += 1
    print(counter, x)
