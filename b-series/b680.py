from functools import total_ordering


@total_ordering
class Player(object):
    def __init__(self, id, time):
        self.id = int(id)
        self.time = float(time)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.time == other.time

    def __lt__(self, other):
        return self.time < other.time


while True:
    try:
        a = int(input())
    except EOFError:
        break
    people = []
    for _ in range(a):
        people.append(Player(*(input().split())))
    people.sort()
    x = a // 8
    for i in range(x):
        print(i+1, end=' ')
        for j in range(8):
            if j == 0:
                print(people[6 * x + i], end=' ')
            elif j == 1:
                print(people[4*x+i], end=' ')
            elif j == 2:
                print(people[2*x+i], end=' ')
            elif j == 3:
                print(people[i], end=' ')
            elif j == 4:
                print(people[2*x-1-i], end=' ')
            elif j == 5:
                print(people[4*x-1-i], end=' ')
            elif j == 6:
                print(people[6*x-1-i], end=' ')
            elif j == 7:
                print(people[8 * x - 1 - i], end=' ')
        print()
