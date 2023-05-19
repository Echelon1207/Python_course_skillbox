my_dict = dict()
while True:
    name = input('Введите имя пользователя: ')
    action = int(input('Введите цифру действия: 1.Посмотреть текущий текст чата.2.Отправить сообщение. : '))
    if action == 1:
        with open('chat.txt','r',encoding='utf8') as file:
            print(file.read())
            file.seek(0)
    if action == 2:
        message = input('Введите сообщение: ')
        my_dict[name] = message
        print(my_dict)
        with open('chat.txt','a',encoding='utf-8') as file:
            for k,v in my_dict.items():
                file.writelines(f'{k} : ')
                file.writelines(v)
                file.writelines('\n')
                print('Сообщение отправлено!')
