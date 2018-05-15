s = input().split()
k = [0,0]
while not s[0] == "Game":
    a = s[1][-1:]
    b = s[1][-1:]
    if a == "s" and b == "e":
        print("靈夢獲勝")
        k[0] += 1
    elif a == "s" and b == "r":
        print("紫獲勝")
        k[1] += 1
    elif a == "e" and b == "r":
        print("靈夢獲勝")
        k[0] += 1
    elif a == "e" and b == "s":
        print("紫獲勝")
        k[1] += 1
    elif a == "r" and b == "e":
        print("紫獲勝")
        k[1] += 1
    elif a == "r" and b == "s":
        print("靈夢獲勝")
        k[0] += 1
    s = input().split()
if k[0] > k[1]:
    print ("悲慘的籌措起香油錢")
else:
    print("螢火的蹤跡")