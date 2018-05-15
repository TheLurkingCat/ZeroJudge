while True:
    try:
        a, b = [int(x) for x in input().split()]
    except EOFError:
        break
    output = [0]*a
    state = {x:x for x in range(1,a+1)}
    for _ in range(b):
        temp = input()
        for i in range(1, a):
            if temp[2*i-1] == '-':
                state[i], state[i+1] = state[i+1], state[i]
    for i, num in enumerate(state.values()):
        output[num-1] = str(i+1)
    print(' '.join(output))