while True:
    month = []
    try:
        for x in range(12):
            month.append(int(input()))
    except EOFError:
        break
    bank = 0
    hand = 0
    for i, money in enumerate(month):
        hand += 300 - money
        if hand < 0:
            print(-i-1)
            break
        save, hand = divmod(hand, 100)
        bank += save
    else:
        print(bank * 120 + hand)
