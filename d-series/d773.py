a = int(input())
s = [x for x in input().split()]
output = []
for i in range(a-1):
    if i == 0:
        if s[0] == '1':
            output.append('x^%d' % (a-i))
        elif s[0] == '-1':
            output.append('-x^%d' % (a-i))
        else:
            output.append(s[0]+'x^%d' % (a-i))
    else:
        if int(s[i]) < 0:
            if s[i] == '-1':
                output.append('-x^%d' % (a-i))
            else:
                output.append(s[i]+'x^%d' % (a-i))
        elif int(s[i]) > 0:
            if s[i] == '1':
                output.append('+x^%d' % (a-i))
            else:
                output.append('+'+s[i]+'x^%d' % (a-i))
last = s.pop()
a = s.pop()
if int(a) < 0:
    if a == '-1':
        output.append('-x')
    else:
        output.append(a+'x')
elif int(a) > 0:
    if a == '1':
        output.append('+x')
    else:
        output.append('+'+a+'x')
if '-' in last:
    output.append(last)
elif last == '0':
    pass
else:
    output.append('+' + last)
print(''.join(output))
