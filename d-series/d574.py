a = input()
try:
    a = int(a)
except ValueError:
    s = a.replace('1000 ', '')
    a = 1000
else:
    s = input()
output = []
count = 0
now = s[0]
for word in s+'!':
    if word == now:
        count += 1
    else:
        output.append('{}{}'.format(count, now))
        now = word
        count = 1
output = ''.join(output)
length = len(output)
print(output if length < a else s)