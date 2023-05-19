import random

num = int(input('Количество чисел в списке: '))
numbers = [random.randint(0, 2) for i in range(num)]

print('Список до сжатия: ', numbers)

new_num = []
for i in numbers:
    if i != 0:
        new_num.append(i)

print('Список после сжатия: ', new_num)

