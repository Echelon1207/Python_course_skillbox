# TODO здесь писать код
def new_contact(my_dict):
    name = input('Введите имя и фамилию нового контакта (через пробел): ')
    number = int(input('Введите номер телефона: '))
    if name in my_dict:
        print('Такой человек уже есть в контактах.')
    else:
        my_dict[name] = number


def search(my_dict):
    surname = input('Введите фамилию для поиска: ').lower()
    for key, val in my_dict.items():
        key_list = key.split(' ')
        if surname == key_list[0][:-1].lower() or surname == key_list[0].lower() or surname[:-1] == key_list[0].lower():
            print(key, val)


my_dict = dict()
while True:
    action = input('Введите номер действия: 1. Добавить контакт , 2. Найти человека : ')
    if action == '1':
        new_contact(my_dict)
    elif action == '2':
        search(my_dict)
    else:
        print('Некорректная цифра')
    print(f'Текущий словарь контактов: {my_dict}')