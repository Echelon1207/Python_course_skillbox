num = int(input('Сколько элементов будет в списке? '))
list = []
new_list = []
for _ in range(num):
    digit = int(input('Введите число: '))
    list.append(digit)
change = int(input('Какой будет сдвиг? '))
print('Изначальный список: ', list)
list = list[-change:] + list[:-change]
print('Сдвинутый список: ', list)
