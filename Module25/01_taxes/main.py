class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_calculation(self):
        pass

class Apartment(Property):

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    def tax_calculation(self):
        return self.worth / 200

class CountryHouse(Property):
    def tax_calculation(self):
        return self.worth / 500



money = int(input('Введите количество денег: '))
property = int(input('Налог на какое имущество будем считать? Дом - 1, Машина -2, Дача - 3: '))
worth = int(input('Введите стоимость имущества: '))

if property == 1:
    apartment = Apartment(worth)
    if money < apartment.tax_calculation():
        lack = apartment.tax_calculation() - money
        print('Налог будет {}.Не хватает {} рублей.'.format(apartment.tax_calculation(), lack))
    else:
        print('Денег хватает,налог будет', apartment.tax_calculation())

elif property == 2:
    car = Car(worth)
    if money < car.tax_calculation():
        lack = car.tax_calculation() - money
        print('Налог будет {}.Не хватает {} рублей.'.format(car.tax_calculation(), lack))
    else:
        print('Денег хватает,налог будет', car.tax_calculation())

elif property == 3:
    country_house = CountryHouse(worth)
    if money < country_house.tax_calculation():
        lack = country_house.tax_calculation() - money
        print('Налог будет {}.Не хватает {} рублей.'.format(country_house.tax_calculation(), lack))
    else:
        print('Денег хватает,налог будет', country_house.tax_calculation())
