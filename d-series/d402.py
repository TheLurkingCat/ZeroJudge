s = []
while True:
    a = input()
    a += '!'
    temp = []
    for word in a:
        if word.isdigit():
            temp.append(word)
        else:
            if temp:
                s.append(int(''.join(temp)))
                temp = []
        if len(s) == 2:
            break
    else:
        continue
    break
print(*s, sum(s))
