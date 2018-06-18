from sys import setrecursionlimit
setrecursionlimit(100000)
ans = str(eval(input()))
print(ans if len(ans) < 5 else ans[-4:])
