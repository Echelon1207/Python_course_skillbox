num = int(input('Введите число: '))
numbers = []
for i in range(1, num+1):
    if i % 2 != 0:
        numbers.append(i)
print(numbers)

