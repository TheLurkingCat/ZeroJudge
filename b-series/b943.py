from cmath import log
a = int(input())
while a:
    z1 = complex(*[float(x) for x in input().split()])
    z2 = complex(*[float(x) for x in input().split()])
    if a & 1:
        ans = z1 ** z2
    else:
        ans = log(z2, z1)
    output = '{:.6f} {} {:.6f}i'
    op = '+' if round(ans.imag, 6) >= 0 else '-'
    print(output.format(round(ans.real, 6), op, abs(round(ans.imag, 6))))
    a = int(input())