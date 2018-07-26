DP = {x: 0 for x in range(1, 201)}
DP[0] = 1
for i in range(1, 201):
    for j in range(i, 201):
        DP[j] += DP[j-i]
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(DP[n])
