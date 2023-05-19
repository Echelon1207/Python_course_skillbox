import random


class House:
    food = 50
    money = 100
    cat_food = 30
    dirt = 0


class Resident:
    def __init__(self, name, satiety, happiness):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        self.satiety += 20
        House.food -= 20
        print(f'{self.name} ест')


class Husband(Resident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)
        self.work = 150

    def work_day(self):
        House.money += self.work
        self.satiety -= 10
        print(f'Муж идет на работу, деньги {House.money}')

    def game(self):
        self.happiness += 20
        self.satiety -= 10
        print('Муж играет')

    def pretting_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('Муж гладит кота')

    def __str__(self):
        return f'{self.name}'


class Wife(Resident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def buy_food(self):
        self.satiety -= 10
        House.food += 50
        House.money -= 50
        print(f'Жена идет в магазин, еда {House.food} деньги {House.money}')

    def buy_cat_food(self):
        self.satiety -= 10
        House.cat_food += 30
        House.money -= 30
        print(f'Жена покупает еду коту, еда кота {House.cat_food} деньги {House.money}')

    def pretting_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('Жена Гладит кота')

    def purchase(self):
        House.money -= 350
        self.happiness += 60
        self.satiety -= 10
        print(f'Жена покупает шубу, деньги {House.money}')

    def cleaning(self):
        House.dirt -= 10
        self.satiety -= 10

    def __str__(self):
        return f'{self.name}'


class Cat(Resident):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety, happiness=100)

    def eat(self):
        self.satiety += 20
        House.cat_food -= 10
        print('Кот ест ')

    def slip(self):
        self.satiety -= 10
        return f'Кот спит'

    def shitting(self):
        self.satiety -= 10
        House.dirt += 5
        print(f'Кот подрал обои')

    def __str__(self):
        return f'{self.name}'


day = 0
husband = Husband(name='Муж')
wife = Wife(name='Жена')
cat = Cat(name='Кот')

for i in range(365):
    day += 1
    print(f'---День {day}')
    House.dirt += 5

    person = random.choice([husband, wife, cat])

    if person.satiety <= 0:
        print(f'К сожалению, {person.name} помер с голоду ')
        break
    if person.happiness <= 10 and not isinstance(person, Cat):
        print(f'К сожалению, {person.name} умер от депрессии ')
        break


    if isinstance(cat, Cat):
        if cat.satiety < 10:
            cat.eat()
        if random.randint(1, 2) == 1:
            cat.shitting()
        elif random.randint(1, 2) == 2:
            print('Кот спит')


    if House.dirt >= 90:
        wife.happiness -= 10
        husband.happiness -= 10

    if isinstance(husband, Husband):
        if House.money <= 150:
            husband.work_day()
        elif husband.happiness <= 50:
            husband.game()
        elif husband.happiness <= 40:
            husband.pretting_cat()
        elif husband.satiety <= 20:
            husband.eat()

    if isinstance(wife, Wife):
        if wife.satiety <= 20:
            wife.eat()
        elif wife.happiness <= 50:
            wife.pretting_cat()
        elif House.money >= 350:
            wife.purchase()
        elif House.food <= 40 and House.money >= 40:
            wife.buy_food()
        elif House.cat_food <= 20:
            wife.buy_cat_food()
        elif House.dirt >= 80:
            wife.cleaning()
            print(f'Жена убирает дом, грязь {House.dirt}')



print(f'Состояние мужа: cчастье:{husband.happiness}, сытость:{husband.satiety}')
print(f'Состояние жены: cчастье:{wife.happiness}, сытость:{wife.satiety}')
print(f'Состояние кота: cчастье:{cat.happiness}, сытость:{cat.satiety}')
print(f'Еды в доме:{House.food} , денег:{House.money}, еды для кота:{House.cat_food}, грязи:{House.dirt}')