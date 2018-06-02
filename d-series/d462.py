while True:
    try:
        a, n, i, k = [int(x) for x in input().split()]
    except EOFError:
        break
    ans = str(pow(a, n))
    print(ans[i-1:i+k-1])
print("From tomcat6 Fri Mar 15 09:53:56 2013\nTo: world\"\nSubject: \"Hello")
