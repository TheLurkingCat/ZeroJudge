n, t = [int(x) for x in input().split()]
score = []
push = score.append
for _ in range(n):
    s, d = [int(x) for x in input().split()]
    i = 1
    while s > 0 or i < t:
        push(s)
        s -= d
        i += 1
score.sort(reverse=True)
print(sum(score[:t]))
