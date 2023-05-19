one = []
two = []
for i in range(3):
    numbers = int(input('Введите число для первого списка: '))
    one.append(numbers)
for i in range(7):
    numbers_two = int(input('Введите число для второго списка: '))
    two.append(numbers_two)
one.extend(two)
unique_numbers = set(one)
unique_list = []
for i in unique_numbers:
    unique_list.append(i)
print(unique_list)