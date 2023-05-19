count = int(input('Введите количество контейнеров: '))
numbers = []
for i in range(count):
    weight = int(input('Введите вес контейнера от 1 до 200: '))
    if weight > 200:
        print('Вес должен быть меньше 200')
        break
    else:
        numbers.append(weight)
new = int(input('Введите вес нового контейнера: '))
numbers.append(new)
numbers.sort(reverse = True)
print(numbers)
print('Номер, который получит новый контейнер: ', numbers.index(new)+1)
