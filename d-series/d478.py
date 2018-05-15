a = input()
while True:
    try:
        first = set(input().split())
    except EOFError:
        break
    second = set(input().split())
    total = len(first & second)
    print(total)