class ParkingLot(object):
    def __init__(self):
        self.parkinglot_by_brand = {}
        self.parkinglot_by_color = {}

    def park(self, car):
        try:
            self.parkinglot_by_brand[car.brand].append(car.color)
        except KeyError:
            self.parkinglot_by_brand[car.brand] = [car.color]
        try:
            self.parkinglot_by_color[car.color].append(car.brand)
        except KeyError:
            self.parkinglot_by_color[car.color] = [car.brand]

    def find_car(self, x, y):
        if x == 'color':
            return self.parkinglot_by_color[y], [y]*len(self.parkinglot_by_color[y])
        return [y]*len(self.parkinglot_by_brand[y]), self.parkinglot_by_brand[y]


class Car(object):
    def __init__(self, brand, color):
        self.color = color
        self.brand = brand


while True:
    try:
        n, m = [int(x) for x in input().split()]
    except EOFError:
        break
    except ValueError:
        continue
    output = []
    parkinglot = ParkingLot()
    for i in range(n):
        brand, color = input().split()
        parkinglot.park(Car(brand, color))
    for i in range(m):
        x, y = input().split()
        x, y = parkinglot.find_car(x, y)
        for a, b in zip(x, y):
            output.append('{} {}'.format(a, b))
    print('\n'.join(output))
