from string import ascii_lowercase, ascii_uppercase, ascii_letters 
intab = ascii_letters
outtab = '{}{}{}{}'.format(ascii_lowercase[3:], 'abc', ascii_uppercase[3:], 'ABC')
trantab = str.maketrans(intab, outtab)
a = int(input())
for _ in range(a):
    x = input()
    print(x.translate(trantab))