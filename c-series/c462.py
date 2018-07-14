from re import search

a = int(input())
base1 = '[A-Z]' * a
base2 = '[a-z]' * a
pattern2 = pattern1 = ''
ans = 0
p1 = True
p2 = True
string = input()
while p1 or p2:
    if ans & 1:
        pattern1 += base2
        pattern2 += base1
    else:
        pattern1 += base1
        pattern2 += base2

    if p1:
        t1 = search(pattern1, string)

        if t1 is None:
            p1 = False
        else:
            ans += 1
            continue

    if p2:
        t2 = search(pattern2, string)
        if t2 is None:
            p2 = False
        else:
            ans += 1
print(ans * a)
