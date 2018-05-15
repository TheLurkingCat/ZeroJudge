s = [int(x) for x in input().split()]
if 6 < s[0] < 17:
    if s[0] == 7 and s[1] < 30:
        print("Off School")
    else:
        print("At School")
else:
    print("Off School")