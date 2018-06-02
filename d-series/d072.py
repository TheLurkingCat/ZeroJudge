x = int(input())
for times in range(1, x+1):
    a = int(input())
    if a % 4 == 0 and a % 100 or a % 400 == 0:
        print("Case {}: a leap year".format(times))
    else:
        print("Case {}: a normal year".format(times))
