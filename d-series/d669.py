while True:
    h1, m1 ,h2, m2 = [int(x) for x in input().split()]
    if h1 or h2 or m1 or m2:
        if h1 == h2:
            if m1 > m2:
                print(1440-m1+m2)
            else:
                print(m2-m1)
        elif h1 < h2:
            m2 += (h2-h1) * 60
            print(m2-m1)
        else:
            m2 += (24-h1+h2) * 60
            print(m2-m1)
    else:
        break