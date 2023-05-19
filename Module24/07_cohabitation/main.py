import random


class Human:
    def __init__(self,name):
        self.name = name
        self.satiety = 50
        self.have_house = True

    def to_eat(self,House):
        self.satiety += 10
        House.eat -= 10
        print("Поели! Сытость у {} - {}. Еды осталось {}".format(self.name,self.satiety,House.eat))
    def earn_money(self,House):
        self.satiety -= 10
        House.money += 10
        print("Поработали! Сытость у {} - {}. Денег осталось {}".format(self.name, self.satiety, House.money))
    def play(self):
        self.satiety -= 10
        print("Поиграли! Сытость у {} - {}".format(self.name,self.satiety))

    def buy_food(self,House):
        House.money -= 10
        House.eat += 10
        print("Купили еду! Денег у {} - {}, еды - {}".format(self.name,House.money,House.eat))

    def live(self,House):

        for _ in range(365):
            num = random.randint(1,6)
            if self.satiety == 0:
                print('Умер')
                break
            else:
                if self.satiety < 20:
                    self.to_eat(House)
                elif House.eat < 10:
                    self.buy_food(House)
                elif House.money < 50:
                    self.earn_money(House)
                elif num == 1:
                    self.earn_money(House)
                elif num == 2:
                    self.to_eat(House)
                else:
                    self.play()
class House:
     eat = 50
     money = 0



man = Human('Tom')
girl = Human('Ann')
man.live(House)
print()
girl.live(House)



