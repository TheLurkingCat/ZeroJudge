"""Numpy solution
from numpy import array, std

output = []
push = output.append

for _ in range(int(input())):
    input()
    ACSB = array([int(x) for x in input().split()])
    push('{:.2f}'.format(std(ACSB)))
    for _ in range(int(input())):
        a, b = (int(x) for x in input().split())
        push('{:.2f}'.format(std(ACSB * a + b)))
    push('')

print(*output, sep='\n')
"""
