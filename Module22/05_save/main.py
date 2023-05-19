import os

name = input('Введите имя файла: ') + '.txt'
save = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split(' ')
path = os.path.join('C:/',*save,name)
chek = os.path.exists(path)

if chek:
    choice = input('Такой файл уже есть. Вы хотите перезаписать его? Y/N').lower()
    if choice == 'y':
        with open(path,'w') as result:
            text = input('Введите текст: ')
            result.write(text)
            print('Файл перезаписан!')
    else:
        print('Файл не перезаписан')
else:
    with open(path, 'w') as result:
        text = input('Введите текст: ')
        result.write(text)
        print('Файл сохранен!')
