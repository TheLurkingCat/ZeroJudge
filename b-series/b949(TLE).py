from math import pow

while True:
    try:
        a = int(input())
    except EOFError:
        break
    print(25 * int(pow(a, 2)))
