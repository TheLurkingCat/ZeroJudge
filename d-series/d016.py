while True:
    try:
        s = [x for x in input().split()]
    except EOFError:
        break
    stack=[]
    for item in s:
        if item.isdigit():
            stack.append(int(item))
        else:
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                stack.append(-1 * stack.pop() + stack.pop())
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            elif item == '%':
                a = stack.pop()
                b = stack.pop()
                stack.append(b%a)
    print(stack.pop())