a = input()
s = [int(x[::-1]) for x in input().split()]
s.sort()
print(s[-1])
