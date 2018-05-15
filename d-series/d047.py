while True:
    try:
        a = int(input())
    except EOFError:
        break
    ordinary = True
    leap = False
    if (a % 4 == 0 and not a % 100 == 0) or a % 400 == 0:
        print("This is leap year.")
        ordinary = False
        leap = True
    if a % 15 == 0:
        print ("This is huluculu festival year.")
        ordinary = False
    if a % 55 == 0 and leap:
        print ("This is bulukulu festival year.")
        ordinary = False
    if ordinary:
        print ("This is an ordinary year.")
    print()