number = int(input('Кол-во чисел: '))
list = []

for i in range(number):
    num = int(input('Число: '))
    list.append(num)

counter = 0
while list != list[::-1]:
    list.insert(number, list[counter])
    counter += 1

print('Нужно приписать чисел:', counter)
print('Сами числа:', list[:counter][::-1])

