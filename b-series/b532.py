a = int(input())
for _ in range(a):
    s = [x for x in input() if x in '0123456789+-*/%']
    temp = ''.join(s)
    temp = temp.replace('/','//')
    temp = temp.replace('*0', '*')
    print(eval(temp))
