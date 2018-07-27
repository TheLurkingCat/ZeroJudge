alphabet = {1: "AMW", 2: "KLY", 3: "JVX",
            4: "HU", 5: "GT", 6: "FS", 7: "ER", 8: "DOQ", 9: "CIP", 10: "BNZ"}
out = []
push = out.append

while True:
    try:
        a = int(input())
    except EOFError:
        break
    a, s = divmod(a, 10)
    for i in range(1, 9):
        a, t = divmod(a, 10)
        s += t * i
    s = 10 - s % 10
    push(alphabet[s])
print(*out, sep='\n')
