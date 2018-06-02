from math import factorial
while True:
    try:
        a = int(input())
    except EOFError:
        break
    print('{}!'.format(a))
    print(factorial(a))
