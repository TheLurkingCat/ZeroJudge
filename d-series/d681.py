while True:
    try:
        output = input().replace('or', '||').replace('and', '&&')
    except EOFError:
        break
    a = output.split()
    output = ''.join(a)
    length = len(a[0])
    temp = str(int(a.pop(0), 2))
    while len(a):
        temp += a.pop(0)[0]
        temp += str(int(a.pop(0), 2))
        temp = str(eval(temp))
    temp = bin(int(temp))[2:]
    length -= len(temp)
    temp = '0'*length + temp
    print('{} = {}'.format(output, temp))
