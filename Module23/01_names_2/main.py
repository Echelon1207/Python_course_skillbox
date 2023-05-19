count = 0
line_count = 0
with open('people','r',encoding='utf-8') as file:
    try:
        for name in file:
            try:
                count+= len(name.rstrip())
                line_count += 1
                if len(name.rstrip()) < 3:
                    raise BaseException
            except BaseException:
                print('Ошибка: Длина {} строки меньше 3х символов'.format(line_count))

    except FileNotFoundError:
        print('Файл не найден')

    finally :
        print('Общее количество символов', count)