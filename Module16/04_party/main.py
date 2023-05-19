guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    name = input('Введите имя гостя: ')
    question = input('Гость пришел или ушел? Пришел/Ушел ').lower()
    if question == 'Пришел':
        guests.append(name)
    elif name not in guests and question == 'ушел':
        print('Такого гостя нет на вечеринке')
    else:
        guests.remove(name)
    sleep = input('Пора спать? Да/Нет').lower()
    if sleep == 'да':
        print('Пока!')
        break
    if len(guests) > 6:
        print('Максимум 6 человек!')
        break
print(guests)