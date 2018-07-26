from calendar import isleap

while True:
    try:
        year = int(input())
    except EOFError:
        break
    print('閏年' if isleap(year) else '平年')
