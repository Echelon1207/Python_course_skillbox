films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []
num = int(input('Сколько фильмов хотите добавить? '))
for i in range(num):
    name = input('Введите название фильма: ')
    if name in films:
        favorite_films.append(name)
    else:
        print('Такого фильма нет в списке')
print(favorite_films)