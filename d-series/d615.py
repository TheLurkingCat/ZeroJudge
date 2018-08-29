from collections import deque

T = int(input())
for _ in range(T):
    s = deque(input().split())
    ans = int(s.popleft())
    while s:
        op = s.popleft()
        if op == '-':
            ans -= int(s.popleft())
        elif op == '*':
            ans *= int(s.popleft())
        elif op == '/':
            ans //= int(s.popleft())
        else:
            ans += int(s.popleft())
    if ans > 9223372036854775807:
        ans %= 9223372036854775808
    print(ans)
