# TODO здесь писать код
def tpl_sort(my_tuple):
    for i in my_tuple:
        if type(i) is not int:
            print('Не все эл-ты кортежа целые числа.')
            return my_tuple
    else:
        return tuple(sorted(my_tuple))


my_tuple = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(my_tuple))