from collections import Counter
a = input()
b = Counter(input())
print(b.most_common()[-1][0])
