from calendar import leapdays
a, b = [int(x) for x in input().split()]
print(leapdays(a, b+1))
