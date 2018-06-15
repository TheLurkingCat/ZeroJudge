d = {x: y for x,  y in enumerate('鼠牛虎兔龍蛇馬羊猴雞狗豬')}
while True:
    try:
        a = int(input())
    except EOFError:
        break
    if a < 0:
        a += 108
    else:
        a -= 1
    a %= 12
    print(d[a])
