a = []
while True:
    try:
        a.append(int(input()))
    except EOFError:
        break
total_steps = {1: 1, 2: 2}
for i in range(3, max(a)+1):
    total_steps[i] = total_steps[i-1] + total_steps[i-2]
ans = [str(total_steps[num]) for num in a]
print('\n'.join(ans))
