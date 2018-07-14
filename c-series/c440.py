from re import sub

k = sub('[^AQ]', '', input())
Q_right = k.count('Q')
Q_left = ans = 0
for word in k:
    if word == 'Q':
        Q_left += 1
        Q_right -= 1
    else:
        ans += Q_left * Q_right
print(ans)
