alphabet = ("BNZ","AMW","KLY","JVX","HU","GT","FS","ER","DOQ","CIP")
while True:
    try:
        a = int(input())
    except EOFError:
        break
    s = a % 10
    a //= 10
    for i in range(1,9):
        s += a % 10 * i
        a //= 10
    s = 10 - s % 10 % 10
    print(alphabet[s])