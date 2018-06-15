from math import sqrt
output = []
push = output.append
while True:
    try:
        a = int(input())
    except Exception:
        break
    total = 0
    while not a & 1:
        a >>= 1
        total += 2
    for i in range(3, round(sqrt(a))+1):
        while not a % i:
            a //= i
            total += i
    a -= 1
    total += a
    total += 1 if a else 0
    push(total)
print(*output, sep='\n')
