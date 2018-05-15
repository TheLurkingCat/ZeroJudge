a = int(input())
s = [0, 0, 0]
while a:
    i = int(input()) % 3
    s[i] += 1
    a -= 1
print(s[0], s[1], s[2])