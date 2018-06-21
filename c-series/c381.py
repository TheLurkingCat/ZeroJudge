from operator import itemgetter
concatenate = ''.join
out = []
push = out.append
while True:
    word = []
    push_word = word.append
    a, b = [int(x) for x in input().split()]
    if a == b == 0:
        break
    for _ in range(a):
        push_word(input())
    t = concatenate(word)
    push(concatenate(itemgetter(
        *[int(x) - 1 for x in input().split()])(t)))
print(*out, sep='\n')
