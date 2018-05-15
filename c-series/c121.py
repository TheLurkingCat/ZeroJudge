def Fibonacci(n):
    backitem1 = 1
    backitem2 = 0
    thisitem = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        thisitem = backitem1 + backitem2
        backitem2, backitem1 = backitem1, thisitem
    return thisitem
while True:
    try:
        a = input()
    except EOFError:
        break      
    ans = "The Fibonacci number for {} is {}".format(a, Fibonacci(int(a)))
    print(ans)
    
