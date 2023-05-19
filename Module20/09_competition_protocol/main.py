# TODO здесь писать код
num = int(input('Сколько записей вносится в протокол? '))

my_list = []
for i in range(num):
    name = input('Введите результат и имя участника через пробел: ').split(' ')
    my_list.append(name)

sort_list = sorted(my_list)
print('Список победителей: ', '1-е место: ',sort_list[-1], '2-е место:', sort_list[-2], '3-е место :', sort_list[-3], sep = '\n')