from functools import reduce
from operator import mul

out = []
push = out.append

a = int(input())

for _ in range(a):
    ans = reduce(mul, (int(x) for x in input()))
    push(ans)
print(*out, sep='\n')
