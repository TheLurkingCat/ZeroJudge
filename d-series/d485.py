a, b = [int(x) for x in input().split()]
print(int(((b - b % 2) - (a + a % 2)) / 2 + 1))
