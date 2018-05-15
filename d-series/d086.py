a = input()
while not a == "0":
    a = a.lower()
    ans = 0
    for word in a:
        if 96 < ord(word) < 123:
            ans += ord(word) - 96
        else:
            print("Fail")
            break
    else:
        print (ans)
    a = input()