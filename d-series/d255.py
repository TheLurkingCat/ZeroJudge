def g(x):
    b = 0
    i = 1
    while i < x :
        j = i + 1
        while j <= x:
            b += gcd(i, j)
            j += 1
        i += 1
    return b
def gcd(a, b):
    while not b == 0:
        a, b = b, a % b
    return a
a = int(input())
while a:
 a = g(a)
 print (a)
 a = int(input())