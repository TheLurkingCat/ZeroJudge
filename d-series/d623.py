def determinan(w, x, y, z):
    return w * z - x * y

while True:
    try:
        w, x = [int(x) for x in input().split()]
        y, z = [int(x) for x in input().split()]
    except ValueError:
        break
    if w or x or y or z:
        k = determinan(w, x, y, z)
        if k:
            w, x, y, z = z/k, -x/k, -y/k, w/k
            print('{:.5f} {:.5f}'.format(w, x))
            print('{:.5f} {:.5f}'.format(y, z))
        else:
            print('cheat!')
    else:
        break