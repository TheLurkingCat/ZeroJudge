ans = 1
for a in range(2, 101):
    ans *= a ** (101-a)
print('\n'.join(list(str(ans))))