# TODO здесь писать код
countries = int(input('Количество стран:  '))
city_dict = dict()

for i in range(countries):
    city = input(' Введите название страны и названия 3х городов в ней через пробел: ').split()
    for j in city[1:]:
         city_dict[j] = city[0]

for i in range(3):
    name = input('Введите название города: ')
    country = city_dict.get(name)
    if country:
        print(f'Город {name} расположен в стране {country}')
    else:
         print(f'По городу {name} нет данных')