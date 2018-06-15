H = '甲乙丙丁戊己庚辛壬癸'
E = '子丑寅卯辰巳午未申酉戌亥'
while True:
    try:
        a = int(input())
    except EOFError:
        break
    a -= 4
    print(H[a % 10], E[a % 12], sep='')
