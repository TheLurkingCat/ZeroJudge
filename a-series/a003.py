state = {0: "普通", 1: "吉", 2: "大吉"}
while True:
    try:
        s = [int(x) for x in input().split()]
    except EOFError:
        break
    k = (s[0] * 2 + s[1]) % 3
    print(state[k])
