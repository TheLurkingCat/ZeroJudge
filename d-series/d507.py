s = [int(x) for x in input().split()]
s.sort()
a2, b2, c2 = [x*x for x in s]
if a2 + b2 > c2:
    print("acute triangle")
elif a2 + b2 == c2:
    print ("right triangle")
else:
    print ("obtuse triangle")