import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health


warrior1=Warrior('Гарри')
warrior2=Warrior('Дементор')

while True:
    num = random.randint(1, 2)
    if num == 1:
        warrior2.health -= 20
        print('Атаковал {}.\nНанесен урон {},его здоровье: {} '.format(warrior1.name,warrior2.name,warrior2.health))
        if warrior2.health <= 0:
            print('Проиграл {}'.format(warrior2.name))
            break
    elif num == 2:
        warrior1.health -= 20
        print('Атаковал {}.\nНанесен урон {},его здоровье: {}'.format(warrior2.name, warrior1.name, warrior1.health))
        if warrior1.health <= 0:
            print('Проиграл {}'.format(warrior1.name))
            break



