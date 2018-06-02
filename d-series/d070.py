a = int(input())
while a:
    a = int(input())
    if a % 4 == 0 and a % 100 or a % 400 == 0:
        print("a leap year")
    else:
        print("a normal year")
