def zashifr():
    shifr = ''
    alfavit_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюяабвгдежзийклмнопрстуфхцчшщьыъэюя'
    step = 3
    text = input('Введите текст: ')
    for i in text:
        find_index = alfavit_ru.find(i)
        new_index = find_index + step
        if i in alfavit_ru:
            shifr += alfavit_ru[new_index]
        else:
            shifr += i
    print(shifr)


zashifr()
