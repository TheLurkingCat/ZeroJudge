translate_table = str.maketrans('hms', ':::')
while True:
    try:
        a = input()
    except EOFError:
        break
    if 'hour' in a:
        ans = int(a.replace('hour', '')) * 3600000
    elif 'min' in a:
        ans = int(a.replace('min', '')) * 60000
    elif 'ms' in a:
        ans = int(a.replace('ms', ''))
    elif 's' in a:
        if '.' in a:
            ans = int(float(a.replace('s', '')) * 1000)
        elif 'm' in a:
            temp = a.translate(translate_table).split(':')
            temp = [int(x) for x in temp if x.isdigit()]
            if 'h' in a:
                ans = temp[0] * 3600000 + temp[1] * 60000 + temp[2] * 1000
            else:
                ans = temp[0] * 60000 + temp[1] * 1000
        else:
            ans = int(a.replace('s', '')) * 1000
    else:
        temp = a.translate(translate_table).split(':')
        temp = [int(x) for x in temp if x.isdigit()]
        ans = temp[0] * 3600000 + temp[1] * 60000
    print(ans)
