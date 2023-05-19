family = {
    'Петров Миша' : 20,
    'Петрова Алина' : 30,
    'Иванов Иван' : 25,
    'Иванова Мария' : 30
    }
surname = input('Введите фамилию: ').lower()

for key,val in family.items():
    key_list = key.split(' ')
    if surname == key_list[0][:-1].lower() or  surname == key_list[0].lower() or surname[:-1] == key_list[0].lower()  :
        print(key,val)

