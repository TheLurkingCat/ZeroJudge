s = [1]
for num in range(500):
    s.append(s[num] + num + 1)
while True:
    try:
        a = int(input())- 1
    except EOFError:
        break    
    print (s[a])
 