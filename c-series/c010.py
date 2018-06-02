from bisect import insort
from array import array
k = array('Q', [])
pointer = 1
output = []
while True:
    try:
        a = int(input())
    except EOFError:
        break
    insort(k, a)
    if pointer & 1:
        output.append(str(k[pointer//2]))
    else:
        x = k[pointer//2]
        y = k[pointer//2-1]
        output.append(str((x+y)//2))
    pointer += 1
print('\n'.join(output))
