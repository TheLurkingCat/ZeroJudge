from collections import Counter
while True:
    output = []
    try:
        a = int(input())
    except EOFError:
        break
    x = Counter(input().split())
    for x ,y in x.most_common():
        output.append(x)
    print(*output)