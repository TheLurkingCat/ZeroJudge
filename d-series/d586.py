to_num = {k: i for i, k in enumerate('uzrmatifxopnhwvbslekycqjgd', 1)}
to_chr = {i: k for i, k in enumerate('mjqhofawcpnsexdkvgtzblryui', 1)}
a = int(input())
for _ in range(a):
    c = input().split()
    del c[0]
    if c[0].isdigit():
        print(''.join([to_chr[int(x)] for x in c]))
    else:
        print(sum([to_num[x] for x in c]))
