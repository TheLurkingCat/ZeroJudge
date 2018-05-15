x = int(input())
dictionary = set()
for _ in range(x):
    dictionary.add(input())
x = int(input())
for _ in range(x):
    c = input()
    if c in dictionary:
        print('yes')
    else:
        print('no')
        dictionary.add(c)
