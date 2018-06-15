from re import sub
while True:
    try:
        s = input()
    except EOFError:
        break
    print(len(sub('[^A-Za-z]', ' ', s).split()))
