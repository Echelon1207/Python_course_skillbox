
class Family:
    surname = 'Nikolaeva'
    earn_money = 100000
    have_house = False

    def info(self):
        print('{}\n{}\n{}\n'.format(self.surname,self.earn_money,self.have_house))

    def earn_to_money(self,new_money):
        self.earn_money += new_money
        print('Новая сумма {}'.format(self.earn_money))

    def bye_house(self,price,discont =0):
        price -= price * (discont/100)
        if self.earn_money >= price:
            self.earn_money -= price
            self.have_house = True
        else:
            print('Недостаточно средств!')



infoo = Family()
infoo.info()

infoo.earn_to_money(100)
infoo.bye_house(80000,10)
infoo.info()
infoo.bye_house(120000)