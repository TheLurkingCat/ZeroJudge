while True:
    try:
        a = input()
    except EOFError:
        break  
    print("'C' can use printf(\"%d\",n); to show integer like", a)
