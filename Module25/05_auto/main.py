import math


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dist, angle):
        self.x = self.x + dist * math.cos(angle)
        self.y = self.y + dist * math.sin(angle)
        print('Едем к координатам', (round(self.x, 2), round(self.y, 2)), 'расстояние: ', dist)

    def __str__(self):
        return f'Координаты машины ({round(self.x, 2)} {round(self.y, 2)})'


class Bus(Car):
    pay = 2
    max_people = 60

    def __init__(self, x, y):
        super().__init__(x, y)
        self.passengers = 0
        self.money = 0

    def move(self, distance, angle):
        self.money += Bus.pay * self.passengers * distance
        print(f'Автобус проехал {distance} км ,водитель заработал {self.money}')

    def enter(self, passengers):
        if self.passengers + passengers > Bus.max_people:
            print(f'Сели в автобус только {Bus.max_people - self.passengers}')
            print(f'Не влезло в автобус {self.passengers + passengers - Bus.max_people}')
            self.passengers = Bus.max_people
        else:
            self.passengers += passengers
            print(f'В автобус сели {passengers} пассажиров')
        return self.passengers

    def exit(self, passengers):
        if self.passengers - passengers < 0:
            print('Все вышли из автобуса')
            self.passengers = 0
        else:
            self.passengers -= passengers
            print(f'Из автобуса вышли {passengers} осталось {self.passengers} пассажиров')
        return self.passengers

    def __str__(self):

        return f'Координаты автобуса ({round(self.x, 2)}, {round(self.y, 2)}).\nВ автобусе {self.passengers} пассажиров.\nВодитель заработал {self.money} рублей'



bus = Bus(x=1, y=2)
bus.enter(50)
bus.move(40, 60)
bus.exit(20)
print(bus)
