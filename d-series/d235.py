i = input()
while not i == "0":
    s = [int(x) for x in i if not x == "\r"]
    chi = 0
    al = 0
    for num in range(len(i)):
        if num % 2:
            al += s[num]
        else:
            chi += s[num]
    if abs(chi - al) % 11:
        print(i, "is not a multiple of 11.")
    else:
        print(i, "is a multiple of 11.")
    i = input()
