a = input()
s = [int(x) for x in input().split()]
s.sort()
s = [str(x) for x in s]
print(' '.join(s))
